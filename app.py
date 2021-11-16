from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from pytube import YouTube
from pytube import Playlist

from PIL import ImageTk, Image
import threading
#from pytube.cli import on_progress

import urllib.request

# Initializing  urllib library for openning URLs
opener = urllib.request.build_opener()
opener.addheaders = [(
    "User-Agent",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36",
)]
urllib.request.install_opener(opener)
# ~~~~


# Main loop
root = Tk()
root.title("YouTube Video Downloader")
# Functions


def download_video():
    print("hello")
    global stream
    """This function starts to download the choosen video"""
    choice = quality_options_choose.get()
    url = video_link_entry.get()
    video = YouTube(url, on_progress_callback=on_progress)
    if choice == quality_options[0]:
        #stream = video.streams.filter(progressive=True).first()
        stream = video.streams.get_highest_resolution()
    elif choice == quality_options[1]:
        stream = video.streams.filter(progressive=True).last()
    stream.download(folder_name)


def on_progress(chunk: bytes, file_handler, bytes_remaining: int):
    global progress
    bytes_downloaded = stream.filesize-bytes_remaining
    print(stream.filesize)
    print(stream.filesize-bytes_remaining)
    progress = (bytes_downloaded/stream.filesize)*100
    print(progress)
    my_label = Label(root, text=f"progress {progress}%")
    my_label.pack()


def open_save_location():
    """This function opens a folder browser to choose where to save your video or playlist"""
    global folder_name
    folder_name = filedialog.askdirectory()
    folder_name_print = Label(root, text=folder_name)
    folder_name_print.pack()
    print(folder_name)


def fetch_info():
    """This function draws video info like thumbnail, length and views"""
    if(r.get() == 1):
        global my_img
        global vid_length
        # print(video_link_entry.get())
        video_link = video_link_entry.get()
        video = YouTube(video_link)
        urllib.request.urlretrieve(  # nosec
            video.thumbnail_url, "video1_thumbnail.png")  # nosec
        image = Image.open("video1_thumbnail.png")
        img = image.resize((300, 200))
        my_img = ImageTk.PhotoImage(img)
        my_label_img = Label(image=my_img)
        my_label_img.pack()
        # print(type(video.streams.filter(progressive=True)))

        vid_length = video.length
        length_label = Label(
            root, text=f"Video length: {vid_length/60} min ")
        length_label.pack()

        vid_title = video.title
        title_label = Label(
            root, text=f"Video title: {vid_title}")
        title_label.pack()

        vid_views = video.views
        views_label = Label(
            root, text=f"Video title: {vid_views}")
        views_label.pack()
        # print(video.streams)


# ~~~~


r = IntVar()
r.set("1")
Radiobutton(root, text="Video", variable=r, value=1).pack()
Radiobutton(root, text="Playlist", variable=r, value=2).pack()

# Global variables
progress = ""
folder_name = ""
my_img = ""
vid_length = ""
# ~~~

# Video URL input
url_label = Label(root, text="Enter Video URL", font=("jost", 15))
url_label.pack()
video_link_entry = Entry(root, width=50, borderwidth=1)
video_link_entry.pack()
submit_url = Button(
    root,
    text="Submit",
    bg="white",
    fg="black",
    command=fetch_info)
submit_url.pack()
# ~~~

# Save location input
choose_location = Button(
    root,
    text="Choose save location",
    bg="white",
    fg="black",
    command=open_save_location,
)
choose_location.pack()
# ~~~

# Video quality input
quality_label = Label(root, text="Select quality", font=("jost", 15))
quality_label.pack()
quality_options = ["720p", "144p"]
quality_options_choose = ttk.Combobox(root, values=quality_options)
quality_options_choose.pack()
# ~~~

# Download button input
download_button = Button(
    root,
    text="Download",
    bg="red",
    fg="white",
    command=lambda: threading.Thread(target=download_video).start())
download_button.pack()
# ~~~


root.mainloop()
# ~~~~
