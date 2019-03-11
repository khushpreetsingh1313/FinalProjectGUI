import time
from tkinter import *
import sqlite3 as GUIdb

import tkinter as mytkint
import csv as file

class GUI:

    #DB = 'FinalProject.db'
    DB = 'fi.db'


    def __init__(self):
        self.species_var = StringVar()
        self.year_var = StringVar()
        self.day_var = StringVar()
        self.number_var = StringVar()
        self.buds_var = StringVar()
        self.numFlower_var = StringVar()
        self.matiurity_var = StringVar()
        self.initials_var = StringVar()
        self.comment_var = StringVar()
        self.widgets()
        self.saveData()
        self.insertData()
        self.Intials





def insertData(self):
    """this insertData function read csv and creating connection as well as inserting row in database. It is also retrieving
    records of database with select query"""

    try:
        path = 'Quttinirpaaq_NP_Tundra_Plant_Phenology_2016-2017_data_1.csv'
        # opening csv file and putting file in object
        with open(path, encoding="ISO-8859-1") as csvfile:
            read = file.reader(csvfile)
            csvList = []
            for data in read:
                csvList.append(data)
         # database name
        #DB = globals()
        con = GUIdb.connect('FinalProject.db') # connection with database
        print("Author is Khushpreet Singh")
        with con:
            cur = con.cursor()
            # creating table if not exists
            cur.execute("create table IF not exists Flower(Species TEXT, year DATE, Julian_Day_of_Year INTEGER,  Plant_Identification_Number INTEGER,  Number_of_Buds INTEGER,  Number_of_Flowers INTEGER,  Number_of_Flowers_that_have_Reached_Maturity INTEGER,  Observer_Initials TEXT,  Observer_Comments TEXT)")

            """Inserting records into Db from arraylist"""
            for i in range(len(csvList)):
                cur.execute("INSERT INTO Flower  VALUES ( ?,?,?,?,?,?,?,?,?)",(csvList[i]))
            print("Loading data........")
            #select all from table flower to display records with cursor
            cur.execute("SELECT * FROM Flower;")
            data = cur.fetchall()
            for d in data:
                print(d)
            print("data loaded sucessfully in database")
    except:
        print("error")
    return self


root = Tk()
species = Label(root,text="species")
species.grid(row=0,column =0,sticky=W)
species_text = Entry(root)

species_text.grid(row=0,column=1)

year = Label(root, text="Year")
year.grid(row=1, column=0,sticky=W)
year_text = Entry(root)
year_text.grid(row=1, column=1)

Day = Label(root, text="Julian Day of Year")
Day.grid(row=2, column=0,sticky=W)
Day_text = Entry(root)
Day_text.grid(row=2, column=1)

Identification = Label(root, text="Plant Identification Number")
Identification.grid(row=3, column=0,sticky=W)
Identification_text = Entry(root)
Identification_text.grid(row=3, column=1)

buds = Label(root, text="Number of Buds")
buds.grid(row=4, column=0,sticky=W)
Buds_text = Entry(root)
Buds_text.grid(row=4, column=1)

flower = Label(root, text="Number of Flowers")
flower.grid(row=5, column=0,sticky=W)
flowers_text = Entry(root)
flowers_text.grid(row=5, column=1)

Maturity = Label(root, text="Number of Flowers that have Reached Maturity")
Maturity.grid(row=6, column=0,sticky=W)
Maturity_text = Entry(root)
Maturity_text.grid(row=6, column=1)


Initials = Label(root, text="Observer Initials")
Initials.grid(row=7, column=0,sticky=W)
Initials_text = Entry(root)
Initials_text.grid(row=7, column=1)

Comments = Label(root, text="Observer Comments")
Comments.grid(row=8, column=0,sticky=W)
Comments_text = Entry(root)
Comments_text.grid(row=8, column=1)

submit = Button(root,text="Submit",anchor=CENTER)
submit.grid(row = 11,column=0)


def saveData(event):

    # database name
    con = GUIdb.connect("FinalProject.db")  # connection with database
    print("Author is Khushpreet Singh")
    with con:
        cur = con.cursor()
        # cur.execute("DROP TABLE IF EXISTS Flower")
        cur.execute("create table IF not exists Flower(Species TEXT, year DATE, Julian_Day_of_Year INTEGER,  Plant_Identification_Number INTEGER,  Number_of_Buds INTEGER,  Number_of_Flowers INTEGER,  Number_of_Flowers_that_have_Reached_Maturity INTEGER,  Observer_Initials TEXT,  Observer_Comments TEXT)")
        insert = "INSERT INTO Flower  VALUES ( ?,?,?,?,?,?,?,?,?)"
        cur.execute(insert, [(species_text.get()), (year_text.get()), (Day_text.get()),
                             (Identification_text.get()), (Buds_text.get()), (flowers_text.get()),
                             (Maturity_text.get()), (Initials_text.get()), (Comments_text.get())])
        cur.execute("SELECT * FROM Flower;")
        data = cur.fetchall()
        for d in data:
            print(d)
    print("Database created")

submit.bind('<Button-1>', saveData)

csvButton = Button(root, text="open csv", anchor=CENTER)
csvButton.grid(row=11, column=1)
csvButton.bind("<Button-1>", insertData)


root.mainloop()

root = Tk()
Label(root,text = "Close me")
time.sleep(2)
obj = GUI()
obj.saveData()
obj.insertData()
