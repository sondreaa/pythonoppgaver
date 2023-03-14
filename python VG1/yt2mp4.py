import tkinter as tk
from pytube import YouTube

root = tk.Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title('yt2mp4')

title = tk.Label(root, text='YOUTUBE VIDEO DOWNLOADER', font='arial 20 bold')
title.pack()

link = tk.StringVar()


paste = tk.Label(root, text = 'Paste Link Here:', font = 'arial 15 bold')
paste.pack()

link_enter = tk.Entry(root, width = 50, textvariable = link)
link_enter.pack()

def Download():
    url = YouTube(str(link.get()))
    #url = YouTube('https://www.youtube.com/watch?v=F4dGW0jHbuo')
    video = url.streams.get_highest_resolution()
    print("Downloading...")
    video.download()
    print("Download completed!!")

knapp = tk.Button(root, text='DOWNLOAD', font = 'arial 15 bold', command = Download, )
knapp.pack()

root.mainloop()

