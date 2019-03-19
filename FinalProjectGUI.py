import time
from tkinter import *
import sqlite3 as GUIdb
import csv as file
from sqlalchemy import  *

listBoxList = []

class GUI():


    DB = 'fi.db'

    def __init__(self):
        self.widgets()
        self.saveData()
        self.insertData()
        self.orminsert()
        self.Intials



def insertData(self):
    """this insertData function read csv and creating connection as well as inserting row in database. It is also retrieving
    records of database """
    csvList = []
    try:
        path = 'Quttinirpaaq_NP_Tundra_Plant_Phenology_2016-2017_data_1.csv'
        # opening csv file and putting file in object
        with open(path, encoding="ISO-8859-1") as csvfile:
            read = file.reader(csvfile)

            for data in read:
                csvList.append(data)

        con = GUIdb.connect("FinalProject.db")  # connection with database
        print("Author is Khushpreet Singh")
        with con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS flowers")
            cur.execute("create table IF not exists flowers(Species TEXT, year DATE, Julian_Day_of_Year INTEGER,  Plant_Identification_Number INTEGER,  Number_of_Buds INTEGER,  Number_of_Flowers INTEGER,  Number_of_Flowers_that_have_Reached_Maturity INTEGER,  Observer_Initials TEXT,  Observer_Comments TEXT)")
            insert = "INSERT INTO flowers  VALUES ( ?,?,?,?,?,?,?,?,?)"
            for i in range(len(csvList)):
                cur.execute(insert, (csvList[i]))

            print("inserted sucessfully")
            print("Developed by Khushpreet Singh")

            cur.execute("SELECT * FROM flowers;")
            data = cur.fetchall()
            Lb1.delete(0, END)
            listBoxList.clear()
            for d in data:
                listBoxList.append(d)
            headers = ["species", "Year", "Julian Day of Year", "Plant Identification Number", "Number of Buds",
                       "Number of Flowers", "Number of Flowers that have Reached Maturity", "Observer Initials",
                       "Observer Comments"]
            row_format = "{:<15s}{:<15s}{:<30s}{:<40s}{:<30s}{:<30s}{:<50s}{:<30s}{:<30s}"
            Lb1.insert(0, row_format.format(*headers, sp=" " * 2))

            for row in listBoxList:
                print(row)
                Lb1.insert(END, row_format.format(*row, sp=" " * 2))
                # print(listBoxList)
    except:
        print("error")
    return "CSVINSERT"

def saveData(event):
    global listBoxList
    # database name
    con = GUIdb.connect("FinalProject.db")  # connection with database
    print("Author is Khushpreet Singh")
    with con:
        cur = con.cursor()
        #cur.execute("DROP TABLE IF EXISTS flowers")
        cur.execute("create table IF not exists flowers(id INTEGER PRIMARY KEY,Species TEXT, year DATE, Julian_Day_of_Year INTEGER,  Plant_Identification_Number INTEGER,  Number_of_Buds INTEGER,  Number_of_Flowers INTEGER,  Number_of_Flowers_that_have_Reached_Maturity INTEGER,  Observer_Initials TEXT,  Observer_Comments TEXT)")
        insert = "INSERT INTO flowers  VALUES ( ?,?,?,?,?,?,?,?,?)"
        cur.execute(insert, [(species_text.get()), (year_text.get()), (Day_text.get()),
                             (Identification_text.get()), (Buds_text.get()), (flowers_text.get()),
                             (Maturity_text.get()), (Initials_text.get()), (Comments_text.get())])
        cur.execute("SELECT * FROM flowers;")
        data = cur.fetchall()
        Lb1.delete(0,END)
        listBoxList.clear()
        for d in data:
            listBoxList.append(d)

        headers = ["ID", "species", "Year", "Julian Day of Year", "Plant Identification Number", "Number of Buds",
                   "Number of Flowers", "Number of Flowers that have Reached Maturity", "Observer Initials",
                   "Observer Comments"]
        row_format = "{:<15s}{:<15s}{:<15s}{:<30s}{:<40s}{:<30s}{:<30s}{:<50s}{:<30s}{:<30s}"
        Lb1.insert(0, row_format.format(*headers, sp=" " * 2))

        for row in listBoxList:
            print(row)
            Lb1.insert(END, row_format.format(*row, sp=" " * 2))

    print("Database created")
    return "db"


len_max = 12

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



submit.bind('<Button-1>', saveData)

csvButton = Button(root, text="insert from csv", anchor=CENTER)
csvButton.grid(row=11, column=1,sticky=W)
csvButton.bind("<Button-1>", insertData)


name = Label(root, text="Khushpreet Singh")
name.grid(row=12, column=0,sticky=W)


Lb1 = Listbox(width = 80)

Lb1.grid(row=0,column=2, rowspan=12,
    padx=5, sticky=E+W+S+N)

headers = ["ID","species","Year","Julian Day of Year", "Plant Identification Number", "Number of Buds","Number of Flowers","Number of Flowers that have Reached Maturity","Observer Initials","Observer Comments"]
row_format ="{:<15s}{:<15s}{:<15s}{:<30s}{:<40s}{:<30s}{:<30s}{:<50s}{:<30s}{:<30s}"
Lb1.insert(0, row_format.format(*headers, sp=" "*2))

root.mainloop()

root = Tk()
Label(root,text = "Close me")
time.sleep(2)
obj = GUI()
obj.saveData()
obj.insertData()
obj.orminsert()
