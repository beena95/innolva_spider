from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
from urllib.parse import urlparse


class UrlDAO:
    """Funzione che , dato un url in input, restituisce un set con gli url al suo interno dello stesso dominio"""

    def get_urls(self, url: str) -> set:

        r = requests.get(url, timeout=1)

        parse_just = SoupStrainer({"a": "href"})
        soup = BeautifulSoup(r.content, "html.parser", parse_only=parse_just)
        local_set = set()
        for tag in soup:
            if self.check_url(tag['href']):
                local_set.add(tag['href'])

        return local_set

    """Funzione che restituisce True se l'url è dello stesso dominio di quello iniziale, altrimenti restituisce False"""

    def check_url(self, url: str) -> bool:
        z = re.search("www.lastampa.it", f"{urlparse(url).netloc}://{urlparse(url).netloc}")
        # t = re.search("archiviolastampa.it", f"{urlparse(url).netloc}://{urlparse(url).netloc}")
        g = re.match('(?:http|ftp|https)://', url)
        if z and g:
            return True
        else:
            return False


if __name__ == '__main__':
    prova = UrlDAO()
    print(prova.get_urls('http://lastampa.it'))
    # for n in prova.get_urls('http://lastampa.it'):
    #     print(n)
