from innolva_spider.model.Article import Article
from bs4 import BeautifulSoup, SoupStrainer
import re
import requests


class ArticleBusiness:

    def download(self, url: str) -> Article:
        """return an Article object from an url in input"""
        soup = self.__soup_url(url)
        return Article(url, self.__get_date(soup), self.__get_author(soup), self.__get_title(soup),
                       self.__get_body(soup))

    def __soup_url(self, url: str):
        """parse an url and return a BeautifulSoup object if the request was successful"""
        try:
            r = requests.get(url)
            parse_only = SoupStrainer(
                {'span': 'entry__date', 'h1': 'entry__title', 'div': ['entry__meta', 'entry__content']})
            soup = BeautifulSoup(r.content, "html.parser", parse_only=parse_only)
            return soup
        except:
            return None

    def __get_date(self, soup: BeautifulSoup):
        """return article publication date"""
        try:
            container = soup.find("span", "entry__date")
            date = container.text.strip("Pubblicato il \n")
            date = date.lstrip()
            return date
        except:
            return None

    def __get_title(self, soup: BeautifulSoup):
        """return article title"""
        try:
            return soup.title.text
        except:
            return None

    def __get_author(self, soup: BeautifulSoup):
        """return article author"""
        try:
            container = soup.find('div', attrs={"class": "entry__meta"}).find("span", "entry__author")
            author = container.text
            return author
        except:
            return None

    def __get_body(self, soup: BeautifulSoup):
        """return article body"""
        try:
            containers = soup.find("div", {"class": "entry__content", "id": "article-body"})
            find_p = containers.find_all("p")
            body = ' '.join(p.text for p in find_p if not p.find("span"))
            body = body.replace("\n", "")
            body = re.sub(r'(?<=[.])', r'\n', body)
            return body
        except:
            return None
