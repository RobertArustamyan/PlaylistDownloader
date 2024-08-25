# YouTube Playlist Downloader

[![YouTube](https://img.shields.io/badge/YouTube-Video-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/)
[![MP3](https://img.shields.io/badge/Audio-MP3-blue?style=for-the-badge&logo=music&logoColor=white)](https://en.wikipedia.org/wiki/MP3)

This project allows you to download audio from YouTube playlist videos and convert them into MP3
format using `yt-dlp` and `pydub`. The project uses Selenium to scrape video links from a playlist
and then downloads mp3 from each video.

## Features

- Scrape video links from YouTube playlists.
- Download audio tracks from YouTube videos.
- Convert downloaded audio into MP3 format.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/PlaylistDownloader.git
   cd PlaylistDownloader
   
2. **Set up environment variables**

   Create a `.env` file in the root directory of project and add playlist link:
   ```shell
   PlaylistLink=https://www.youtube.com/playlist?list=YourPlaylist

## Usage

1. **Export YouTube cookies using Cookie Quick Manager:**

   - Install the [Cookie Quick Manager](https://addons.mozilla.org/en-US/firefox/addon/cookie-quick-manager/) extension if you use Firefox.
   - Export your YouTube cookies as a JSON file and save them in root directory of project.
2. **Run the downloader**
   ```shell
   python main.py
   ```

## Licence
This project is licensed under the MIT License. See the  `LICENSE` file for details.
