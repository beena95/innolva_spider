import time
from innolva_spider.dao.UrlDAO import UrlDAO
from innolva_spider.dao.ArticleToDB import ArticleToDB
from innolva_spider.business.ArticleBusiness import ArticleBusiness


def timer(func):
    def wrapper(*args, **kwargs):
        """returns the time of execution"""
        start_time = time.time()
        ret_value = func(*args, **kwargs)
        end_time = time.time()
        num_seconds = end_time - start_time
        print("- Time for compute \'" + func.__name__ + "\':" + str(round(num_seconds, 4)) + " s")
        return ret_value

    return wrapper


class UrlBusiness:

    def __init__(self):
        self.url_dao = UrlDAO()
        self.articles_to_db = ArticleToDB()
        self.a_business = ArticleBusiness()
        self.setArticles = set()

    def take_urls(self, set_non_vis: set) -> set:
        """Save visited and unvisited links and downloaded articles inside the respective collections"""
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
        """Download articles"""
        article = self.a_business.download(url)
        if article.body:
            # self.setArticles.add(article)
            self.articles_to_db.save(article, "ARTICLES_COLLECTION")

    @timer
    def go_deep(self, level: int, url: str):
        """Crawls inside the url extracting links until it reaches the level of depth
        and save the unvisited links in the respective collection"""
        # gestire get primo url
        # if url:
        set_non_vis = self.url_dao.get_urls(url)
        # cancella elementi delle collection per i test
        self.articles_to_db.clear_collection("VISITATI")
        self.articles_to_db.clear_collection("ARTICLES_COLLECTION")
        self.articles_to_db.clear_collection("NON VISITATI")
        # else:
        #     set_non_vis = self.articles_to_db.links_list("NON VISITATI")
        print(len(set_non_vis))
        while level > 0:
            set_non_vis = self.take_urls(set_non_vis)
            level -= 1
        self.articles_to_db.save_list(set_non_vis, "NON VISITATI")


if __name__ == '__main__':
    prova = UrlBusiness()
    p = prova.go_deep(2)

    # count = 0
    # for article in p:
    #     count += 1
    #     if count == 10:
    #         break
    #     print(article.url, article.date, article.author, article.title, article.body)
