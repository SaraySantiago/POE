from tkinter import *

def key(event):
    print("Has pulsado la tecla", repr(event.char))

def callback(event):
    frame.focus_set()
    print("Has hecho click en", event.x, event.y)

root = Tk()

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()