from innolva_spider.dao.ArticleToDB import ArticleToDB
from innolva_spider.model.Article import Article
from bs4 import BeautifulSoup
import re
import requests


class ArticleBusiness:

    database = ArticleToDB("mongodb+srv://username:password@dbarticles-qv1r7.mongodb.net/test?retryWrites=true&w=majority", "DBARTICLES")

    def __init__(self, url):
        self.url = url
        self.soup = self.soup_url()
        self.article = Article(self.url, self.get_date(), self.get_author(), self.get_title(), self.get_body())

    # def url_to_mongodb(self):
    #     self.database.object_to_dict(self.article, "articles_collection")

    """Restituisce un oggetto BeautifulSoup se la richiesta di connessionee va a buon fine"""

    def soup_url(self):
        try:
            r = requests.get(self.url)
            soup = BeautifulSoup(r.content, "html.parser")
            return soup
        except:
            return None

        # except ConnectionError as e:
        #     print("handling a ", type(e))  # controlla (, o format) stampare stack

    """Dato un url, restituisce la data pubblicazione"""

    def get_date(self):
        try:
            container = self.soup.find("span", "entry__date")
            date = container.text.strip("Pubblicato il \n")
            date = date.lstrip()
            return date
        except:
            return None

    """Dato un url, restituisce il titolo"""

    def get_title(self):
        try:
            return self.soup.title.text
        except:
            return None

    """Dato un url, restituisce l'autore"""

    def get_author(self):
        try:
            container = self.soup.find('div', attrs={"class": "entry__meta"}).find("span", "entry__author")
            author = container.text
            return author
        except:
            return None

    """Dato un url, restituisce il corpo"""

    def get_body(self):
        try:
            containers = self.soup.find("div", {"class": "entry__content", "id": "article-body"})
            find_p = containers.find_all("p")
            body = ' '.join(p.text for p in find_p if not p.find("span"))
            body = body.replace("\n", "")
            body = re.sub(r'(?<=[.])', r'\n', body)
            return body
        except:
            return None
