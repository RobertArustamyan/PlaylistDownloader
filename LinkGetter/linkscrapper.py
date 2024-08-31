from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()


class LinksParser:
    """
    Class that extracts URL links of videos from playlist.
    NOTE: Playlist must be public!
    """
    def __init__(self):
        self.options = None
        self.service = None
        self.driver = None
        self.__initializeDriver()
        self.loadDriver()

    def __initializeDriver(self):
        """
        Initializes selenium driver and sets settings.
        """
        self.options = Options()
        self.options.binary_location = '/home/robert/Applications/firefox-127.0b6/firefox/firefox-bin'
        self.service = Service('/usr/bin/geckodriver')
        self.options.add_argument('--headless')

    def loadDriver(self):
        """
        Loads selenium driver.
        """
        self.driver = webdriver.Firefox(service=self.service, options=self.options)

    def _playlistConnection(self, link):
        """
        Send get request to playlist url.
        :param link: Url of playlist.
        """
        self.driver.get(link)

    def playlistHtml(self, link):
        """
        Extracts HTML page of playlist.
        :param link: Url of playlist.
        :return: Html page of playlist.
        """
        self._playlistConnection(link=link)
        self.driver.implicitly_wait(30)

        scroll_pause_time = 2  # Pause to allow content to load
        last_height = self.driver.execute_script("return document.documentElement.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = self.driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        return self.driver.page_source

    @staticmethod
    def getLinks(html):
        """
        Extracts URLs from source page.
        :param html: HTML of page.
        :return: URL of videos in playlist.
        """
        soup = BeautifulSoup(html, 'lxml')
        thumbnails = soup.find_all('a', id='thumbnail')
        urls = []
        for a in thumbnails:
            href = a.get('href')
            if href:
                urls.append('https://www.youtube.com' + href)
        return urls[1:]

    def playlistLinks(self, link):
        """
        Connecting all functions of class in one.
        :param link: Url of playlist.
        :return: Returns links of videos.
        """
        plHtml = self.playlistHtml(link=link)
        links = self.getLinks(html=plHtml)
        self.driver.quit()
        return links


if __name__ == '__main__':
    parser = LinksParser()
    print(parser.playlistLinks(os.getenv('PlaylistLink')))
