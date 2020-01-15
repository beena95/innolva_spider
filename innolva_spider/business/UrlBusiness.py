import time
from datetime import datetime

from innolva_spider.dao.UrlRequestDAO import UrlRequestDAO
from innolva_spider.business.ArticleBusiness import ArticleBusiness


def timer(func):
    def wrapper(*args, **kwargs):
        """return the time of execution"""
        start_time = datetime.now()
        ret_value = func(*args, **kwargs)
        end_time = datetime.now()
        num_seconds = end_time - start_time
        print("- Time for compute \'" + func.__name__ + "\':" + str(num_seconds) + " s")
        return ret_value

    return wrapper


class UrlBusiness:

    def __init__(self):
        self.url_request = UrlRequestDAO()
        self.articles_to_db = ArticleToDB()
        self.a_business = ArticleBusiness()
        self.setArticles = set()

    def take_urls(self, set_unvis: set) -> set:
        """crawl inside each url, update the collections, return a set of unvisited urls"""
        set_vis = self.articles_to_db.links_list("VISITED")
        set_urls = set_unvis.difference(set_vis)
        for url in set_urls:
            try:
                set_to_check = self.url_request.get_urls(url)
                # set_unvis = url_dao_mongo.check_visited(set_to_check)

            except:
                continue
            self.articles_to_db.save("VISITED", url)
            self.add_article(url)

        print(len(set_unvis))
        set_unvis.difference_update(set_urls)
        print(len(set_unvis))
        return set_unvis

    def add_article(self, url):
        """download articles and add them in the respective collection"""
        article = self.a_business.download(url)
        if article.body:
            # self.setArticles.add(article)
            self.articles_to_db.save("ARTICLES", article)

    @timer
    def go_deep(self, level: int, url: str):
        """crawl inside the url until the level of depth is reached,
        save the unvisited links in the respective collection"""
        # gestire get primo url
        # if url:
        set_unvis = self.url_request.get_urls(url)
        # cancella elementi delle collection per i test
        self.articles_to_db.clear_collection("VISITED")
        self.articles_to_db.clear_collection("ARTICLES")
        self.articles_to_db.clear_collection("UNVISITED")
        # else:
        #     set_non_vis = self.articles_to_db.links_list("NON VISITATI")
        print(len(set_unvis))
        while level > 0:
            set_unvis = self.take_urls(set_unvis)
            level -= 1
        self.articles_to_db.save_list("UNVISITED", set_unvis)


if __name__ == '__main__':
    test = UrlBusiness()
    t = test.go_deep(2, "http://www.lastampa.it")

    # count = 0
    # for article in p:
    #     count += 1
    #     if count == 10:
    #         break
    #     print(article.url, article.date, article.author, article.title, article.body)
