import tkinter as tk
from vidstream import ScreenShareClient
import sys

sender = ScreenShareClient('192.168.1.69', 9999)

def screenshare():
    sender.start_stream()

def stahpit():
    sender.stop_stream()
    sys.exit()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                    text="Exit", 
                    fg="red",
                    command=stahpit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                    text="Screenshare",
                    command=screenshare)
slogan.pack(side=tk.LEFT)

root.mainloop()
