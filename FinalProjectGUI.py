from tkinter import *
import tkinter as mytkint
import csv as file

class GUI:

    def __init__(self):
        # self.species = StringVar()
        # self.year = StringVar()
        # self.day = StringVar()
        # self.number = StringVar()
        # self.buds = StringVar()
        # self.numFlower = StringVar()
        # self.matiurity = StringVar()
        # self.initials = StringVar()
        # self.comment = StringVar()
        self.widgets()
        self.saveData()


    def saveData(self):
        print("i am clicked")
        return self

    def widgets(self):

        self.species = StringVar()
        self.year = StringVar()
        self.day = StringVar()
        self.number = StringVar()
        self.buds = StringVar()
        self.numFlower = StringVar()
        self.matiurity = StringVar()
        self.initials = StringVar()
        self.comment = StringVar()

        root = Tk()
        species = Label(root,text="species")
        species.grid(row=0,column =0,sticky=W)
        species_text = Entry(root, textvariable = self.species)
        species_text.grid(row=0,column=1)

        year = Label(root, text="Year")
        year.grid(row=1, column=0,sticky=W)
        year_text = Entry(root,textvariable = self.year)
        year_text.grid(row=1, column=1)

        Day = Label(root, text="Julian Day of Year")
        Day.grid(row=2, column=0,sticky=W)
        Day_text = Entry(root,textvariable = self.day)
        Day_text.grid(row=2, column=1)

        Identification = Label(root, text="Plant Identification Number")
        Identification.grid(row=3, column=0,sticky=W)
        Identification_text = Entry(root,textvariable = self.number)
        Identification_text.grid(row=3, column=1)

        species = Label(root, text="Number of Buds")
        species.grid(row=4, column=0,sticky=W)
        species_text = Entry(root,textvariable = self.buds)
        species_text.grid(row=4, column=1)

        Buds = Label(root, text="Number of Flowers")
        Buds.grid(row=5, column=0,sticky=W)
        Buds_text = Entry(root,textvariable = self.numFlower)
        Buds_text.grid(row=5, column=1)

        Maturity = Label(root, text="Number of Flowers that have Reached Maturity")
        Maturity.grid(row=6, column=0,sticky=W)
        Maturity_text = Entry(root,textvariable = self.matiurity)
        Maturity_text.grid(row=6, column=1)


        Initials = Label(root, text="Observer Initials")
        Initials.grid(row=7, column=0,sticky=W)
        Initials_text = Entry(root,textvariable = self.initials)
        Initials_text.grid(row=7, column=1)

        Comments = Label(root, text="Observer Comments")
        Comments.grid(row=8, column=0,sticky=W)
        Comments_text = Entry(root,textvariable = self.comment)
        Comments_text.grid(row=8, column=1)

        submit = Button(root,text="Submit",anchor=CENTER)
        submit.grid(row = 11,column=0)

        submit.bind("<Button-1>", lambda e:self.saveData())



        root.mainloop()

root = Tk()
obj = GUI()
obj.widgets()
obj.saveData()
