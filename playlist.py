# System Imports
import threading
# GUI Imports
import tkinter as tk
from tkinter import Label, Entry, Button, StringVar, filedialog, IntVar, Checkbutton
from tkscrolledframe import ScrolledFrame
# Pytube Imports
from pytube import Playlist
from pytube import YouTube


def set_window():
    # configuring up the window layout and position
    root.title("YouTube Video Downloader")
    # icon = PhotoImage(file='./1002.png')
    # window.iconphoto(True, icon)
    window_width = 500
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


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


def draw():
    """
        This function is called by the "Submit Link" Button
        It draws each video information on the playlist like video title, size, qualities and checkboxes
        After the video information are drawn, it starts to draw the download button
    """
    stream_lst_2 = []
    # Initialize variables and objects
    playlist_link = video_link_entry.get()
    playlist = Playlist(playlist_link)

    global var
    global services
    i = 1
    k = 0
    services = []
    # Start drawing each video information by iterating through the playlist
    rows = 2
    cols = 0
    for video in playlist.videos:
        Label(frame, text=f"Video {i}").grid(row=rows, column=cols)
        rows += 1
        Label(frame, text=f"Title: {video.title[0:50]}").grid(
            row=rows, column=cols)
        rows += 1
        # Video quality and size
        fetch_quality_info(video.embed_url)
        Label(frame, text=" ".join(str(x)
              for x in available_res)).grid(row=rows, column=cols)
        rows += 1
        Label(frame, text=" ".join(str(x)
              for x in sizes)).grid(row=rows, column=cols)
        rows += 1
        # Video quality checkbox for downloading later

        for res in available_res:
            option = IntVar()
            option.set(0)
            services.append(option)
            Checkbutton(frame, text=f"Download {res}",
                        variable=services[k]).grid(row=rows, column=cols)
            rows += 1
            k += 1
        Label(frame, text="-"*60).grid(row=rows, column=cols)
        rows += 1
        i += 1

    # The download button
    download_button2 = Button(
        frame,
        text="Download Checked",
        bg="red",
        fg="white", command=lambda: threading.Thread(target=download_video_2).start(),
        width=18, border=0.5, pady=0, padx=0, font=("Aerial", 9))
    download_button2.grid(row=3, column=1)

    # # Checkbox selection submission
    # Button(frame, text="Submit Selections",
    #        command=show,
    #        width=18, border=0.5, pady=0, padx=0, font=("Aerial", 9)
    #        ).grid(row=4, column=1)


def show():
    """
        This function makes a global list of the selections of videos which will be later used to download
    """
    global selected
    global ls
    ls = []
    for i in range(len(services)):
        selected = ""
        if services[i].get() >= 1:
            print(services[i].get())
            selected += str(i)
            ls.append(str(i))
            # print(selected)
    print(ls)
    print(services)


# def download_video():
#     """
#         Here we download each video by iterating through the playlist
#     """
#     url = video_link_entry.get()
#     playlist = Playlist(url)
#     global stream_lst
#     stream_lst = []
#     urls = []

#     # Making urls list
#     for video in playlist.videos:
#         urls.append(video.embed_url)
#     j = 0

#     # Making stream list
#     for video in playlist.videos:
#         for i in available_res:
#             v = YouTube(urls[j], on_progress_callback=on_progress)
#             stream = v.streams.filter(
#                 progressive=True).get_by_resolution(i)
#             if stream != None:
#                 stream_lst.append(stream)
#         j += 1
#     # print(stream_lst)

#     # Downloading each stream individually
#     # print(stream_lst)
#     for i in ls:
#         stream_lst[int(i)].download(folder_name)


def download_video_2():
    show()
    url = video_link_entry.get()
    #playlist = Playlist(url)
    #urls = []
    #print("hello")
    #print(stream_lst_2)
    # for p in playlist.videos:
    #     p.register_on_progress_callback(on_progress)
    k = 1
    for i in ls:
        # print(i)
        progress.set(f"Downloading Video {k}")
        #print(f"Downloading this {stream_lst_2[int(i)]}")
        stream_lst_2[int(i)].download(folder_name)
        progress.set(f"Done Downloading")
        k += 1


# def on_progress(chunk: bytes, file_handler, bytes_remaining: int):
#     """
#         This function is responsible for the progress meter for each video being downloaded
#     """
#     global my_label
#     count = 1
#     for i in stream_lst:
#         bytes_downloaded = i.filesize-bytes_remaining
#         # print(i.filesize)
#         # `print(i.filesize-bytes_remaining)
#         progress2 = (bytes_downloaded/i.filesize)*100
#         progress.set(f"progress {count}: "+str(round(progress2))+"%")
#         # my_label = Label(frame, text=f"progress {progress}%")
#         # my_label.grid()
#         count += 1
#         frame.update_idletasks()
#         break


def open_save_location():
    """
        This function opens a folder browser to choose where to save your video or playlist
    """
    global folder_name
    folder_name = filedialog.askdirectory()
    folder_name_print = Label(
        frame, text=folder_name, font=("Aerial", 8), width=21)
    folder_name_print.grid(row=4, column=1)


def fetch_quality_info(video_link):
    """
        This function takes argument video link and make two global lists
        available_res: a list of all available resolutions for this specific video link
        sizes: a list of the corresponding sizes of each available resolution
    """
    global sizes
    global available_res

    video = YouTube(video_link)
    available_res = []

    stream = video.streams.filter(
        progressive=True).get_by_resolution("720p")
    if(stream != None):
        available_res.append("720p")
        stream_lst_2.append(stream)

    stream = video.streams.filter(
        progressive=True).get_by_resolution("480p")
    if(stream != None):
        available_res.append("480p")
        stream_lst_2.append(stream)

    stream = video.streams.filter(
        progressive=True).get_by_resolution("360p")
    if(stream != None):
        available_res.append("360p")
        stream_lst_2.append(stream)

    stream = video.streams.filter(
        progressive=True).get_by_resolution("144p")
    if(stream != None):
        available_res.append("144p")
        stream_lst_2.append(stream)

    sizes = []
    for i in available_res:
        stream = video.streams.filter(
            progressive=True).get_by_resolution(i)
        if(stream != None):
            sizes.append(str(round(stream.filesize/(1024*1024)))+" MB")


global stream_lst_2
stream_lst_2 = []

Label(frame, text="Enter playlist URL", justify='center',  font=("Arial", 25), padx=10).grid(
    row=0, column=0)


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
    font=("Aerial", 9)
)
submit_url_button.grid(row=1, column=1)

progress = StringVar()
my_label = Label(frame, textvariable=progress, font=("Aerial", 8), width=21)
my_label.grid(row=5, column=1)

choose_location = Button(
    frame,
    text="Choose Save Location",
    bg="white",
    fg="black",
    command=open_save_location,
    width=18, border=0.5, pady=0, padx=0, font=("Aerial", 9)
)
choose_location.grid(row=2, column=1)

root.mainloop()
