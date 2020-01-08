from innolva_spider.dao.UrlDAO import UrlDAO
from innolva_spider.dao.ArticleToDB import ArticleToDB

import time
import re
import requests
from urllib.parse import urlparse

from innolva_spider.business.ArticleBusiness import ArticleBusiness


class UrlBusiness:
    def __init__(self):
        self.url_dao = UrlDAO()
        self.articles_to_db = ArticleToDB()
        self.setArticles = set()

    """Funzione che salva url non visitati, visitati e articoli scaricati"""

    def take_urls(self, set_non_vis: set) -> set:
        set_vis = self.articles_to_db.sync_set()
        set_urls = set_non_vis.difference(set_vis)
        for url in set_urls:
            self.articles_to_db.delete_by_condition_dict("NON VISITATI", {"URL": url})
            try:
                set_non_vis = set_non_vis.union(self.url_dao.get_urls(url))
            except:
                continue
            self.articles_to_db.save(url, "VISITATI")
            if ArticleBusiness(url).getBody():
                url_article = ArticleBusiness(url).article
                # self.setArticles.add(url_article)
                self.articles_to_db.save(url_article, "ARTICLES_COLLECTION")

        print(len(set_non_vis))
        set_non_vis.difference_update(set_urls)
        print(len(set_non_vis))
        self.articles_to_db.save(set_non_vis, "NON VISITATI")
        return set_non_vis

    """Funzione che dato, un url ed un livello di difficoltà, scava all'interno dell'url cercando altri url"""

    def go_deep(self, livello: int, url: str = ""):
        #gestire get primo url
        if url:
            set_non_vis = self.url_dao.get_urls(url)
        else:
            set_non_vis = self.articles_to_db.sync_set()
        print(len(set_non_vis))
        print(set_non_vis)
        while livello > 0:
            set_non_vis = self.take_urls(set_non_vis)
            livello -= 1


if __name__ == '__main__':

    prova = UrlBusiness()
    p = prova.go_deep(2, "https://www.lastampa.it/")

    # count = 0
    # for article in p:
    #     count += 1
    #     if count == 10:
    #         break
    #     print(article.url, article.date, article.author, article.title, article.body)
