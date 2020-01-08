
from innolva_spider.dao.UrlDAO import UrlDAO
from innolva_spider.dao.ArticleToDB import ArticleToDB

import time
import re
import requests
from urllib.parse import urlparse

from innolva_spider.business.ArticleBusiness import ArticleBusiness


class UrlBusiness():
    def __init__(self):
        self.url_dao = UrlDAO()
        self.articles_to_db = ArticleToDB()
        self.setArticles = set()


    def takeUrls(self, setNonVis:set) -> set:
        setVis = self.articles_to_db.sync_set(self.fileVisitati)
        setUrls = setNonVis.difference(setVis)
        for url in setUrls:
            self.articles_to_db.delete_by_condition_dict("NON VISITATI", {"URL": url})
            try:
                setNonVis = setNonVis.union(self.url_dao.getUrls(url))
            except:
                continue
            self.articles_to_db.save(url, "VISITATI")
            if ArticleBusiness(url).getBody():
                url_article = ArticleBusiness(url).article
                # self.setArticles.add(url_article)
                self.articles_to_db.save(url_article, "ARTICLES_COLLECTION")

        print('lunghezza set articoli: ', len(self.setArticles))
        print(self.setArticles)
        print(len(setNonVis))
        setNonVis.difference_update(setUrls)
        print(len(setNonVis))
        self.articles_to_db.save(setNonVis, "NON VISITATI")
        return setNonVis






    def goDeep(self, livello:int, url:str = ""):
        if url:
            setNonVis = self.url_dao.getUrls(url)
        else:
            setNonVis = self.file_dao.sync_set(self.fileNonVisitati)
        print(len(setNonVis))
        print(setNonVis)
        while livello>0:
            setNonVis = self.takeUrls(setNonVis)
            livello -= 1

        return self.setArticles




if __name__ == '__main__':


    prova = UrlBusiness()
    p = prova.goDeep(2, "https://www.lastampa.it/")

    # count = 0
    # for article in p:
    #     count += 1
    #     if count == 10:
    #         break
    #     print(article.url, article.date, article.author, article.title, article.body)

