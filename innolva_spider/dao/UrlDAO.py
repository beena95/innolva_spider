from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
from urllib.parse import urlparse


class UrlDAO:

    def get_urls(self, url: str) -> set:
        """parse an url and return a set containing urls from the same domain"""
        r = requests.get(url, timeout=1)
        parse_just = SoupStrainer({"a": "href"})
        soup = BeautifulSoup(r.content, "html.parser", parse_only=parse_just)
        local_set = set()
        for tag in soup:
            if self.check_url(tag['href']):
                local_set.add(tag['href'])

        return local_set

    def check_url(self, url: str) -> bool:
        """return True if the url is in the same domain"""
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
