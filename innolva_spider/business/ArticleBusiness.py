from innolva_spider.model.Article import Article
from bs4 import BeautifulSoup, SoupStrainer
import re
import requests


class ArticleBusiness:

    # def __init__(self, url):
    #     self.url = url
    #     self.soup = self.soup_url()
    #     self.article = Article(self.url, self.get_date(), self.get_author(), self.get_title(), self.get_body())

    def download(self, url):
        soup = self.__soup_url(url)
        return Article(url, self.__get_date())

    def __soup_url(self, url: str):
        """Restituisce un oggetto BeautifulSoup se la richiesta di connessionee va a buon fine"""
        try:
            r = requests.get(url)
            parse_only = SoupStrainer(
                {'span': 'entry__date', 'h1': 'entry__title', 'div': ['entry__meta', 'entry__content']})
            soup = BeautifulSoup(r.content, "html.parser", parse_only=parse_only)
            return soup
        except:
            return None

    """Dato un url, restituisce la data pubblicazione"""

    def __get_date(self, soup: BeautifulSoup):
        try:
            container = self.soup.find("span", "entry__date")
            date = container.text.strip("Pubblicato il \n")
            date = date.lstrip()
            return date
        except:
            return None

    """Dato un url, restituisce il titolo"""

    def __get_title(self, soup: BeautifulSoup):
        try:
            return self.soup.title.text
        except:
            return None

    """Dato un url, restituisce l'autore"""

    def __get_author(self, soup: BeautifulSoup):
        try:
            container = self.soup.find('div', attrs={"class": "entry__meta"}).find("span", "entry__author")
            author = container.text
            return author
        except:
            return None

    """Dato un url, restituisce il corpo"""

    def __get_body(self, soup: BeautifulSoup):
        try:
            containers = self.soup.find("div", {"class": "entry__content", "id": "article-body"})
            find_p = containers.find_all("p")
            body = ' '.join(p.text for p in find_p if not p.find("span"))
            body = body.replace("\n", "")
            body = re.sub(r'(?<=[.])', r'\n', body)
            return body
        except:
            return None
