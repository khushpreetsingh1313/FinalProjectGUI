from tkinter import *
from random import randint
import random

root = Tk()

width = 400
height = width
colors = ["red", "orange", "yellow", "green", "blue", "violet", "white"]
dropcount = width // 2
drops = []

background = Canvas(root, width=width, height=height, background='black')
background.pack()


class Drop():
    def __init__(self, locationx, locationy, heightdrop, widthdrop, color):
        self.locationx = locationx
        self.locationy = locationy
        self.heightdrop = heightdrop
        self.widthdrop = widthdrop
        self.color = color

    def newdrop(self):
        drop = background.create_rectangle(self.locationx, self.locationy, self.locationx + self.widthdrop,
                                           self.locationy + self.heightdrop, fill=self.color)
        drops.append(drop)


for i in range(dropcount):
    drop = Drop(randint(0, width), randint(-100, 100), 10, 2, random.choice(colors))
    drop.newdrop()


def move_drops():
    for drop in drops:
        background.move(drop, 0, 5)
    root.after(100, move_drops)


root.after(100, move_drops)
root.mainloop()

root.mainloop()