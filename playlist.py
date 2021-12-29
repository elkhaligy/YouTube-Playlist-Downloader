"""Imports"""
# System Imports
import threading
# GUI Imports
import tkinter as tk
from tkinter import Label, Entry, Button, StringVar, filedialog, IntVar, Checkbutton, messagebox
from tkinter.messagebox import NO
from tkscrolledframe import ScrolledFrame
# Pytube Imports
from pytube import Playlist
from pytube import YouTube
####
"""Global Variables"""
global stream_list
stream_list = []
####
"""Functions"""


def set_window():
    # configuring up the window layout and position
    root.title("YouTube Video Downloader")
    window_width = 500
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


def draw():
    """
        This function is called by the "Submit Link" Button
        It draws each video information on the playlist like video title, size, qualities and checkboxes
        After the video information are drawn, it starts to draw the download button
    """
    global var
    global services
    # Initialize variables and objects
    playlist_link = video_link_entry.get()
    try:
        playlist = Playlist(playlist_link)

        i = 1
        k = 0
        services = []
        # Start drawing each video information by iterating through the playlist
        rows = 2
        coselected_boxes = 0
        for video in playlist.videos:
            Label(frame, text=f"Video {i}").grid(row=rows,
                                                 column=coselected_boxes)
            rows += 1
            Label(frame, text=f"Title: {video.title[0:50]}").grid(
                row=rows, column=coselected_boxes)
            rows += 1
            # Video quality and size
            get_quality_sizes(video.embed_url)
            Label(frame, text=" ".join(str(x) for x in available_res)).grid(
                row=rows, column=coselected_boxes)
            rows += 1
            Label(frame,
                  text=" ".join(str(x)
                                for x in sizes)).grid(row=rows,
                                                      column=coselected_boxes)
            rows += 1
            # Video quality checkbox for downloading later

            for res in available_res:
                option = IntVar()
                option.set(0)
                services.append(option)
                Checkbutton(frame,
                            text=f"Download {res}",
                            variable=services[k]).grid(row=rows,
                                                       column=coselected_boxes)
                rows += 1
                k += 1
            Label(frame, text="-" * 60).grid(row=rows, column=coselected_boxes)
            rows += 1
            i += 1

        # The download button
        download_button = Button(
            frame,
            text="Download Checked",
            bg="red",
            fg="white",
            command=lambda: threading.Thread(target=start_download).start(),
            width=18,
            border=0.5,
            pady=0,
            padx=0,
            font=("Aerial", 9))
        download_button.grid(row=3, column=1)

        download_all_button = Button(
            frame,
            text="Download All",
            bg="red",
            fg="white",
            command=lambda: threading.Thread(target=download_all).start(),
            width=18,
            border=0.5,
            pady=0,
            padx=0,
            font=("Aerial", 9))
        download_all_button.grid(row=4, column=1)
    except:
        try:
            video = YouTube(playlist_link)
            i = 1
            k = 0
            services = []
            # Start drawing each video information by iterating through the playlist
            rows = 2
            coselected_boxes = 0
            Label(frame, text=f"Video {i}").grid(row=rows,
                                                 column=coselected_boxes)
            rows += 1
            Label(frame, text=f"Title: {video.title[0:50]}").grid(
                row=rows, column=coselected_boxes)
            rows += 1
            # Video quality and size
            get_quality_sizes(video.embed_url)
            Label(frame, text=" ".join(str(x) for x in available_res)).grid(
                row=rows, column=coselected_boxes)
            rows += 1
            Label(frame,
                  text=" ".join(str(x)
                                for x in sizes)).grid(row=rows,
                                                      column=coselected_boxes)
            rows += 1
            # Video quality checkbox for downloading later

            for res in available_res:
                option = IntVar()
                option.set(0)
                services.append(option)
                Checkbutton(frame,
                            text=f"Download {res}",
                            variable=services[k]).grid(row=rows,
                                                       column=coselected_boxes)
                rows += 1
                k += 1
            Label(frame, text="-" * 60).grid(row=rows, column=coselected_boxes)
            rows += 1
            i += 1

            # The download button
            download_button = Button(frame,
                                     text="Download Checked",
                                     bg="red",
                                     fg="white",
                                     command=lambda: threading.Thread(
                                         target=start_download).start(),
                                     width=18,
                                     border=0.5,
                                     pady=0,
                                     padx=0,
                                     font=("Aerial", 9))
            download_button.grid(row=3, column=1)
        except:
            messagebox.showerror('Error', 'Please enter a valid url!')
            print("Something went wrong")


def get_selected_boxes():
    """
        This function makes a global list of the selections of videos which will be later used to download
    """
    #global selected
    global selected_boxes
    selected_boxes = []
    for i in range(len(services)):
        #selected = ""
        if services[i].get() >= 1:
            # print(services[i].get())
            #selected += str(i)
            selected_boxes.append(str(i))
            # print(selected)
    # print(selected_boxes)


def start_download():
    get_selected_boxes()
    k = 1
    # print(stream_list)
    for i in selected_boxes:
        # print(i)
        progress.set(f"Downloading Video {k}")
        #print(f"Downloading this {stream_list[int(i)]}")
        stream_list[int(i)].download(folder_name)
        progress.set(f"Done Downloading")
        k += 1
        messagebox.showinfo('News', 'Videos are downloaded successfully!')

def download_all():
    k = 1
    playlist_link = video_link_entry.get()
    playlist = Playlist(playlist_link)
    for video in playlist.videos:
        # print(i)
        progress.set(f"Downloading Video {k}")
        stream = video.streams.filter(
            progressive=True).get_highest_resolution()
        if stream != None:
            stream.download(folder_name)
        # stream_list[int(i)].download(folder_name)
        progress.set(f"Done Downloading")
        k += 1
    messagebox.showinfo('News', 'Playlist is downloaded successfully!')


def open_save_location():
    """
        This function opens a folder browser to choose where to save your video or playlist
    """
    global folder_name
    folder_name = filedialog.askdirectory()
    folder_name_print = Label(frame,
                              text=folder_name,
                              font=("Aerial", 8),
                              width=21)
    folder_name_print.grid(row=5, column=1)


def get_quality_sizes(video_link):
    """
        This function takes argument video link and make two global lists
        available_res: a list of all available resolutions for this specific video link
        sizes: a list of the corresponding sizes of each available resolution
    """
    global sizes
    global available_res

    video = YouTube(video_link)
    available_res = []
    stream = video.streams.filter(only_audio=True)[0]
    if (stream != None):
        available_res.append("Audio")
        stream_list.append(stream)

    stream = video.streams.filter(progressive=True).get_by_resolution("720p")
    if (stream != None):
        available_res.append("720p")
        stream_list.append(stream)

    stream = video.streams.filter(progressive=True).get_by_resolution("480p")
    if (stream != None):
        available_res.append("480p")
        stream_list.append(stream)

    stream = video.streams.filter(progressive=True).get_by_resolution("360p")
    if (stream != None):
        available_res.append("360p")
        stream_list.append(stream)

    stream = video.streams.filter(progressive=True).get_by_resolution("144p")
    if (stream != None):
        available_res.append("144p")
        stream_list.append(stream)

    sizes = []
    for i in available_res:
        if (i == "720p" or i == "480p" or i == "360p" or i == "144p"):
            stream = video.streams.filter(
                progressive=True).get_by_resolution(i)
            if (stream != None):
                sizes.append(
                    str(round(stream.filesize / (1024 * 1024))) + " MB")
        else:
            stream = video.streams.filter(only_audio=True)[0]
            sizes.append(str(round(stream.filesize / (1024 * 1024))) + " MB")


#####
"""Main Window"""
# Create a root window
root = tk.Tk()
#root.title("YouTube Video Downloader")
set_window()
frame_top = tk.Frame(root, width=500, height=400)
frame_top.pack(side="top", expand=1, fill="both")

# Create a ScrolledFrame widget
sf = ScrolledFrame(frame_top, width=500, height=400)
sf.pack(side="top", expand=1, fill="both")

# Bind the arrow keys and scroll wheel
sf.bind_arrow_keys(frame_top)
sf.bind_scroll_wheel(frame_top)

frame = sf.display_widget(tk.Frame)

Label(frame,
      text="Enter playlist URL",
      justify='center',
      font=("Arial", 25),
      padx=10).grid(row=0, column=0)

video_link_entry = Entry(frame, width=50, borderwidth=1)
video_link_entry.grid(row=1, column=0, padx=10)

submit_url_button = Button(
    frame,
    text="Submit Link",
    bg="white",
    fg="black",
    command=lambda: threading.Thread(target=draw).start(),
    width=18,
    border=0.5,
    pady=0,
    padx=0,
    font=("Aerial", 9))
submit_url_button.grid(row=1, column=1)

progress = StringVar()
my_label = Label(frame, textvariable=progress, font=("Aerial", 8), width=21)
my_label.grid(row=6, column=1)

choose_location = Button(frame,
                         text="Choose Save Location",
                         bg="white",
                         fg="black",
                         command=open_save_location,
                         width=18,
                         border=0.5,
                         pady=0,
                         padx=0,
                         font=("Aerial", 9))
choose_location.grid(row=2, column=1)

root.mainloop()
#####
