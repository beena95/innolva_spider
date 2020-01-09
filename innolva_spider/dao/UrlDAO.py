from multiprocessing.pool import Pool

from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
from urllib.parse import urlparse
from html.parser import HTMLParser


class UrlDAO:

    # def __init__(self):
    #     self.s = set()

    def get_urls(self, url: str):

        r = requests.get(url, timeout=1)
        parse_only = SoupStrainer({'a':'href'})
        soup = BeautifulSoup(r.content, parse_only = parse_only)
        s = set()



        # for tag in soup.findAll():
        #     s.add(tag)


        for tag in soup.findAll('a'):
            if self.check_url(tag['href']):
                s.add(tag['href'])


        return s

    def check_url(self, url: str) -> bool:
        z = re.search("www.lastampa.it", f"{urlparse(url).netloc}://{urlparse(url).netloc}")
        # t = re.search("archiviolastampa.it", f"{urlparse(url).netloc}://{urlparse(url).netloc}")
        g = re.match('(?:http|ftp|https)://', url)
        if z and g:
            return True
        else:
            return False

    def pool_get_urls(self, subprocesses:int = 5):
        pool = Pool(subprocesses)
        with pool as p:
            set_urls = p.map(self.get_urls(), self.get_urls(self.url))
        return set_urls

if __name__ == '__main__':

    prova = UrlDAO()
    print(len(prova.get_urls('http://lastampa.it')))
    for n in prova.get_urls('http://lastampa.it'):
        print(n)
