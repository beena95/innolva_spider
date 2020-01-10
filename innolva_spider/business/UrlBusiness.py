import time
from multiprocessing.pool import Pool

from innolva_spider.dao.UrlDAO import UrlDAO
from innolva_spider.dao.ArticleToDB import ArticleToDB
from innolva_spider.business.ArticleBusiness import ArticleBusiness


# import time
#
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         ret_value = func(*args, **kwargs)
#         end_time = time.time()
#         num_seconds = end_time - start_time
#         print("- Time for compute \'" + func.__name__ + "\':" + str(round(num_seconds, 4)) + " s")
#         return ret_value
#
#     return wrapper


class UrlBusiness:

    def __init__(self):
        self.url_dao = UrlDAO()
        self.articles_to_db = ArticleToDB()
        self.setArticles = set()

    def timer(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            ret_value = func(*args, **kwargs)
            end_time = time.time()
            num_seconds = end_time - start_time
            print("- Time for compute \'" + func.__name__ + "\':" + str(round(num_seconds, 4)) + " s")
            return ret_value

        return wrapper

    """Funzione che salva url non visitati, visitati e articoli scaricati"""

    def take_urls(self, set_non_vis: set) -> set:
        set_vis = self.articles_to_db.links_list("VISITATI")
        set_urls = set_non_vis.difference(set_vis)
        for url in set_urls:
            try:
                set_non_vis = set_non_vis.union(self.url_dao.get_urls(url))
            except:
                continue
            self.articles_to_db.save(url, "VISITATI")
            self.add_article(url)

        print(len(set_non_vis))
        set_non_vis.difference_update(set_urls)
        print(len(set_non_vis))
        return set_non_vis

    def add_article(self, url):
        if ArticleBusiness(url).get_body():
            url_article = ArticleBusiness(url).article
            # self.setArticles.add(url_article)
            self.articles_to_db.save(url_article, "ARTICLES_COLLECTION")

    """Funzione che dato, un url ed un livello di difficoltà, scava all'interno dell'url cercando altri url"""

    @timer
    def go_deep(self, livello: int, url: str = ""):
        # gestire get primo url
        if url:
            set_non_vis = self.url_dao.get_urls(url)
            # cancella elementi delle collection per i test
            self.articles_to_db.clear_collection("VISITATI")
            self.articles_to_db.clear_collection("ARTICLES_COLLECTION")
            self.articles_to_db.clear_collection("NON VISITATI")
        else:
            set_non_vis = self.articles_to_db.links_list("NON VISITATI")
        print(len(set_non_vis))
        print(set_non_vis)
        while livello > 0:
            set_non_vis = self.take_urls(set_non_vis)
            livello -= 1
        self.articles_to_db.save_list(set_non_vis, "NON VISITATI")



if __name__ == '__main__':

    prova = UrlBusiness()
    # p = prova.go_deep(2, "https://www.lastampa.it/")
    urls = []
    pool = Pool(10)
    pool.starmap(prova.go_deep(2, "https://www.lastampa.it/"), urls)
    pool.terminate()
    pool.join()

    # count = 0
    # for article in p:
    #     count += 1
    #     if count == 10:
    #         break
    #     print(article.url, article.date, article.author, article.title, article.body)
