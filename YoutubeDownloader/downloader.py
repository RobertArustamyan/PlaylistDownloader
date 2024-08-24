import yt_dlp
from pydub import AudioSegment
import os


class YouTubeDownloader:
    def __init__(self, urls):
        self.urls = urls

    def downloadMP3(self, output_path='Playlists'):
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        for url in self.urls:
            try:
                cleanUrl = url.split('&')[0]

                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'cookies': '../cookies.json'
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([cleanUrl])

                print(f"Downloaded and converted: {cleanUrl}")
            except Exception as e:
                print(f"Failed to download {url}: {e}")


if __name__ == '__main__':
    links = \
        ['https://www.youtube.com/watch?v=hqqkyyjAJis&list=PLu3AETzBHBLwgkry7ZenIDxoxGpIXkeSZ&index=1&pp=iAQB8AUB',
         'https://www.youtube.com/watch?v=DTz5k-8AzJo&list=PLu3AETzBHBLwgkry7ZenIDxoxGpIXkeSZ&index=2&pp=iAQB8AUB']


    downloader = YouTubeDownloader(links)
    downloader.downloadMP3()
