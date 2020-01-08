from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urlparse
from html.parser import HTMLParser


class UrlDAO:

    # def __init__(self):
    #     self.s = set()

    def get_urls(self, url: str):

        r = requests.get(url, timeout=1)
        soup = BeautifulSoup(r.content)
        s = set()

        for tag in soup.findAll('a', href=True):
            if self.check_url(tag['href']):
                s.add(tag['href'])
                # self.uV.addUrl(tag['href'], text)

        return s

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
    print(len(prova.get_urls('http://lastampa.it')))
    for n in prova.get_urls('http://lastampa.it'):
        print(n)
