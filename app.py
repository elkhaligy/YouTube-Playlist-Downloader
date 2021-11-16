from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from pytube import Playlist
from PIL import ImageTk, Image
root = Tk()
folder_name = ""
# function to get the name of save location
place_holder = Entry(root, text='  ', font=("jost", 15))
place_holder.grid(row=0, column=0, columnspan=3)


def open_save_location():
    global folder_name
    folder_name = filedialog.askdirectory()
    folder_name_print = Label(root, text=folder_name)
    folder_name_print.grid(row=1, column=3)

    print(folder_name)
   # if(len(folder_name) > 1):
    #    locationError.config(text=folder_name, fg="green")
   # else:
    #    locationError.config(text="Please choose folder",fg="red")

# function to start downloading a video


def download_video():
    choice = quality_options_choose.get()
    url = video_link_entry.get()
    video = YouTube(url)
    if(choice == quality_options[0]):
        stream = video.streams.filter(progressive=True).first()
    elif(choice == quality_options[1]):
        stream = video.streams.filter(progressive=True).last()
    stream.download(folder_name)


# title and geometry of the app window
root.title("YouTube Video Downloader")
root.geometry("700x400")
root.columnconfigure(0, weight=1)

# obtaining video link from the user
text_1 = Label(root, text='Enter Video/Playlist URL', font=("jost", 15))
text_1.grid(row=1, column=0)

video_link_entry = Entry(root, width=50, borderwidth=0)
video_link_entry.grid()

# choosing save location

#text_2 = Label(root, text='Choose save location', font=("jost", 15))
# text_2.grid()

save_location_entry = Button(
    root, text="Choose location", width=10, bg="white", fg="black", padx=15, pady=5, command=open_save_location)
save_location_entry.grid(row=1, column=1)

# choosing video quality
text_3 = Label(root, text='Select quality', font=("jost", 15))
text_3.grid()

quality_options = ["720p", "144p"]
quality_options_choose = ttk.Combobox(root, values=quality_options)
quality_options_choose.grid()

# start download
download_button = Button(root, text="Download", width=10,
                         bg="red", fg="white", command=download_video)
download_button.grid()
root.mainloop()
