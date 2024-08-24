from LinkGetter.linkscrapper import LinksParser
from YoutubeDownloader.downloader import YouTubeDownloader
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    linkParser = LinksParser()
    links = linkParser.playlistLinks(os.getenv('PlaylistLink'))

    downloader = YouTubeDownloader(urls=links)
    downloader.downloadMP3()