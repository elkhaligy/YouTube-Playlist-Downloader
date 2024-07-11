# YouTube Playlist Downloader

YouTube Playlist Downloader is a Python application that allows you to download individual YouTube videos or entire playlists. The application provides a graphical user interface (GUI) for ease of use.

## Features

- Download individual YouTube videos.
- Download entire YouTube playlists.
- Choose the video quality before downloading.
- Display video information such as title, length, views, and size.
- Choose the location to save the downloaded videos.

## Requirements

- Python 3.x
- `pytube` library
- `Pillow` library
- `tkinter` library
- `tkscrolledframe` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/YouTube-Playlist-Downloader.git
    cd YouTube-Playlist-Downloader
    ```

2. Install the required libraries:
    ```bash
    pip install pytube Pillow tkscrolledframe
    ```

## Usage

### Download a Single Video

1. Run the `app.py` script:
    ```bash
    python app.py
    ```

2. Enter the URL of the video you want to download.
3. Choose the download location.
4. Select the desired video quality.
5. Click the "Download" button.

### Download a Playlist

1. Run the `playlist.py` script:
    ```bash
    python playlist.py
    ```

2. Enter the URL of the playlist you want to download.
3. Choose the download location.
4. Select the videos and qualities you want to download.
5. Click the "Download Checked" button to download selected videos or "Download All" to download the entire playlist.

## File Descriptions

- `app.py`: Script for downloading individual YouTube videos.
- `playlist.py`: Script for downloading entire YouTube playlists.
- `README.md`: This file.

## Acknowledgements

This project uses the following open-source libraries:

- [pytube](https://github.com/nficano/pytube)
- [Pillow](https://python-pillow.org/)
- [tkinter](https://wiki.python.org/moin/TkInter)
- [tkscrolledframe](https://github.com/bducrot/tkscrolledframe)
