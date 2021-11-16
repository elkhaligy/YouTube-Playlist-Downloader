from tkinter import *
from pytube import YouTube
from pytube import Playlist
from PIL import ImageTk, Image
import urllib.request
import requests
# Adding information about user agent
opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

root = Tk()
root.geometry('910x400')
b1 = Button(root, text="Video link(entry)", width=40)
b1.grid(row=0, column=0, padx=0, pady=0)

b11 = Button(root, text="Submit", width=10)
b11.grid(row=0, column=1, padx=0, pady=0)

b2 = Button(root, text="Save location(button)", width=40)
b2.grid(row=0, column=2)

b3 = Button(root, text="Save path(label)", width=40)
b3.grid(row=0, column=3, padx=10, pady=10)

b4 = Button(root, text="Video thumbnail(png)", width=40, height=12)
b4.grid(row=1, column=0, columnspan=1, rowspan=3)

b5 = Button(root, text="Video title(label)", height=3, width=15)
b5.grid(row=1, column=1, sticky=NW)

b6 = Button(root, text="Video size(label)", height=3, width=15)
b6.grid(row=2, column=1, sticky=W)

b7 = Button(root, text="Download(button)", height=3, width=15)
b7.grid(row=3, column=1,  sticky=SW)

#video = YouTube('https://www.youtube.com/watch?v=668nUCeBHyY')


# print(video.thumbnail_url)


#urllib.request.urlretrieve(video.thumbnail_url, "video1_thumbnail.png")


#my_img = ImageTk.PhotoImage(Image.open("video1_thumbnail.png"))


#my_label = Label(image=my_img)


#my_label.grid(row=0, column=0)

root.mainloop()
