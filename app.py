from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from pytube import Playlist
from PIL import ImageTk, Image
import urllib.request

# Initializing  urllib library for openning URLs
opener = urllib.request.build_opener()
opener.addheaders = [
    (
        "User-Agent",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36",
    )
]
urllib.request.install_opener(opener)

# Functions
def download_video():
    choice = quality_options_choose.get()
    url = video_link_entry.get()
    video = YouTube(url)
    if choice == quality_options[0]:
        stream = video.streams.filter(progressive=True).first()
    elif choice == quality_options[1]:
        stream = video.streams.filter(progressive=True).last()
    stream.download(folder_name)


def open_save_location():
    global folder_name
    folder_name = filedialog.askdirectory()
    folder_name_print = Label(root, text=folder_name)
    folder_name_print.grid()
    print(folder_name)


def fetch_thumbnail():
    global my_img
    print(video_link_entry.get())
    video_link = video_link_entry.get()
    video = YouTube(video_link)
    urllib.request.urlretrieve(video.thumbnail_url, "video1_thumbnail.png")
    image = Image.open("video1_thumbnail.png")
    img = image.resize((300, 200))
    my_img = ImageTk.PhotoImage(img)
    my_label = Label(image=my_img)
    my_label.grid(row=0, column=0)


# Main loop
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("")

# Global variables
folder_name = ""
my_img = ""
# ~~~

# Video URL input
text_1 = Label(root, text="Enter Video URL", font=("jost", 15))
text_1.grid()
video_link_entry = Entry(root, width=50, borderwidth=1)
video_link_entry.grid()
get_thumbnail = Button(
    root, text="Submit", bg="white", fg="black", command=fetch_thumbnail
)
get_thumbnail.grid()
# ~~~

# Save location input
choose_location = Button(
    root,
    text="Choose save location",
    bg="white",
    fg="black",
    command=open_save_location,
)
choose_location.grid()
# ~~~


# Video quality input
text_3 = Label(root, text="Select quality", font=("jost", 15))
text_3.grid()
quality_options = ["720p", "144p"]
quality_options_choose = ttk.Combobox(root, values=quality_options)
quality_options_choose.grid()
# ~~~

# Download button input
download_button = Button(
    root, text="Download", bg="red", fg="white", command=download_video
)
download_button.grid()
# ~~~


root.mainloop()
# ~~~~
