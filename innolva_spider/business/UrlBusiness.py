import time
from datetime import datetime
from innolva_spider.dao.UrlDAO import UrlDAO
from innolva_spider.dao.ArticleDAO import ArticleDAO
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
        self.url_dao = UrlDAO()
        self.articles_dao = ArticleDAO()
        self.a_business = ArticleBusiness()
        self.setArticles = set()

    def check_urls_in_collection(self, url):
        for url in self.url_request.get_urls(url):
            try:
                if not self.url_dao.check_visited(url, "VISITED"):
                    self.url_dao.save_url("UNVISITED", url)
            except:
                continue


    def take_urls(self):
        """crawl inside each url, update the collections"""
        print(len(self.url_dao.all_urls("UNVISITED")))
        for url in self.url_dao.all_urls("UNVISITED"):
            try:
                self.check_urls_in_collection(url)
            except:
                continue
            self.url_dao.save_url("VISITED", url)
            self.url_dao.delete_url(url, "UNVISITED")
            self.add_article(url)


    def add_article(self, url):
        """download articles and add them in the respective collection"""
        article = self.a_business.download(url)
        if article.body:
            # self.setArticles.add(article)
            self.articles_dao.save_url("ARTICLES", article)

    @timer
    def go_deep(self, level: int, url: str):
        """crawl inside the url until the level of depth is reached,
        save the unvisited links in the respective collection"""
        # gestire get primo url
        self.articles_dao.clear_collection("VISITED")
        self.articles_dao.clear_collection("ARTICLES")
        self.articles_dao.clear_collection("UNVISITED")
        self.check_urls_in_collection(url)
        print(len(self.url_dao.all_urls("UNVISITED")))
        # cancella elementi delle collection per i test

        while level > 0:
            self.take_urls()
            level -= 1



if __name__ == '__main__':
    test = UrlBusiness()
    t = test.go_deep(2, "http://www.lastampa.it")

    # count = 0
    # for article in p:
    #     count += 1
    #     if count == 10:
    #         break
    #     print(article.url, article.date, article.author, article.title, article.body)
