from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from pytube import Playlist
from PIL import ImageTk, Image
import urllib.request


root = Tk()
root.geometry('910x400')

# Adding information about user agent
opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


def fetch_thumbnail():
    print(b1.get())
    video_link = b1.get()
    video = YouTube(video_link)
    urllib.request.urlretrieve(video.thumbnail_url, "video1_thumbnail.png")
    image = Image.open('video1_thumbnail.png')
    img = image.resize((300, 200))
    my_img = ImageTk.PhotoImage(img)
    my_label = Label(image=my_img)
    my_label.grid()



# Video link entry
b1 = Entry(root, text="Video link(entry)", width=40, borderwidth=1)
b1.insert(0, 'Video link')
b1.grid(row=0, column=0)
b11 = Button(root, text="Submit", width=10,
             borderwidth=1, command=fetch_thumbnail)
b11.grid()


def on_click(event):
    b1.configure(state=NORMAL)
    b1.delete(0, END)
    # make the callback only work once
    b1.unbind('<Button-1>', on_click_id)


on_click_id = b1.bind('<Button-1>', on_click)
# ~~~~

# Video thumbnail

#video = YouTube('https://www.youtube.com/watch?v=668nUCeBHyY')
#urllib.request.urlretrieve(video.thumbnail_url, "video1_thumbnail.png")


# b4 = Button(root, text="Video thumbnail(png)",borderwidth = 1, width = 50, height = 10)
# b4.grid(row=2, column=0, rowspan=3)


# ~~~~
print(b1.get())
root.mainloop()
