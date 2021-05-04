from tkinter import *

top = Tk()
songList = []

def addTrack():
    songList.append(E1.get())
    print(songList)

    
L1 = Label(top, text="Hello world!")
L1.grid(column= 0, row= 1)

E1 = Entry(top, bd = 5)
E1.grid(column= 0, row = 2)

B1 = Button(text = "Add to Playlist", bg = "flesh", command= addTrack
B1.grid(column= 1, row = 2)
print(E1.get())

top.mainloop()
