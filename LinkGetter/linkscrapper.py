from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()


class LinksParser:
    def __init__(self):
        self.options = None
        self.service = None
        self.driver = None
        self.__initializeDriver()
        self.loadDriver()

    def __initializeDriver(self):
        self.options = Options()
        self.options.binary_location = '/home/robert/Applications/firefox-127.0b6/firefox/firefox-bin'
        self.service = Service('/usr/bin/geckodriver')
        self.options.add_argument('--headless')

    def loadDriver(self):
        self.driver = webdriver.Firefox(service=self.service, options=self.options)

    def _playlistConnection(self, link):
        self.driver.get(link)

    def playlistHtml(self, link):
        self._playlistConnection(link=link)
        self.driver.implicitly_wait(30)
        return self.driver.page_source

    def getLinks(self, link):
        pageHtml = self.playlistHtml(link=link)
        soup = BeautifulSoup(pageHtml, 'lxml')

        thumbnails = soup.find_all('a', id='thumbnail')
        urls = []
        for a in thumbnails:
            href = a.get('href')
            if href:
                urls.append('https://www.youtube.com' + href)
        return urls[1:]


if __name__ == '__main__':
    parser = LinksParser()
    print(parser.getLinks(os.getenv('PlaylistLink')))
