import sqlite3
from tkinter import Button, Label
from tkinter.ttk import Entry


class car():  ####################################################  trunck manage

    def __init__(self, master):

        ##super(car,self).__init__()
        ##        tk.Frame.__init__(self, master)

        self.master = master
        ##self.master.geometry('500x600+100+200')
        self.master.geometry('600x500')
        self.master.title('Report')
        self.button28 = Button(self.master, text="create", command=self.tabluh1)
        self.button28.grid(row=0, column=0)

        self.button29 = Button(self.master, text="insert rec", command=self.insertar1)
        self.button29.grid(row=3, column=2)

        self.tyLabel1 = Label(self.master, text="driver name")
        self.tyLabel1.grid(row=1, column=0)

        self.disLabel1 = Label(self.master, text="trunck type")
        self.disLabel1.grid(row=2, column=0)

        self.pelLabel1 = Label(self.master, text="pelack")
        self.pelLabel1.grid(row=3, column=0)

        self.d = Entry(self.master)
        self.d.grid(row=1, column=1)

        self.e = Entry(self.master)
        self.e.grid(row=2, column=1)

        self.f = Entry(self.master)
        self.f.grid(row=3, column=1)

        self.connection = sqlite3.connect('jadval.db')
        self.cur = self.connection.cursor()
        self.dateLabel1 = Label(self.master, text="driver name", width=10)
        self.dateLabel1.grid(row=4, column=0)
        self.BMILabel1 = Label(self.master, text="trunck type", width=10)
        self.BMILabel1.grid(row=4, column=1)
        self.stateLabel1 = Label(self.master, text="pelack", width=10)
        self.stateLabel1.grid(row=4, column=2)

        self.button1 = Button(self.master, text='OK', command=self.get_list)
        self.button1.grid(row=6, column=3)

        ##        self.enter1 = Entry(self.master, bg='yellow')
        ##        self.enter1.grid(row=8, column=3)

        self.readfromdatabase1()
        ##self.showallrecords1()

    ##    def showallrecords1(self):
    ##
    ##        data1 = self.readfromdatabase1()
    ##        for index1, dat1 in enumerate(data1):
    ##            Label(self.master, text=dat1[0]).grid(row=index1+5, column=0)
    ##            Label(self.master, text=dat1[1]).grid(row=index1+5, column=1)
    ##            Label(self.master, text=dat1[2]).grid(row=index1+5, column=2)

    def tabluh1(self):
        ##pragma encoding=utf8;
        c.execute('''CREATE TABLE trunmanage(id1 INTEGER,firs1 stringvar(10),las1 stringvar(10))''')
        ##c.execute('''CREATE TABLE trunmanage(id1 INTEGER,firs1 stringvar(10),las1 stringvar(10))''')

    def insertar1(self):

        d1 = self.d.get()
        e1 = self.e.get()
        f1 = int(self.f.get())
        c.execute("INSERT INTO trunmanage (id1, firs1,las1 ) VALUES (?, ?, ?)", (f1, d1, e1))
        conn.commit()
        self.readfromdatabase1()
        ##self.showallrecords1()

    def readfromdatabase1(self):
        self.cur.execute("SELECT * FROM trunmanage")
        ##return self.cur.fetchall()
        rows = self.cur.fetchall()
        for row in rows:
            ##lb1 = Listbox(self.master)
            self.lb1 = Listbox(self.master)

            ##lb1.grid(row=5)
            self.lb1.grid(row=5)

        for item in rows:
            ##lb1.insert(END, item)
            self.lb1.insert(END, item)

    def get_list(self):
        """
        function to read the listbox selection
        and put the result in an entry widget
        """
        global enter1

        # get selected line index

        ##index = lb1.curselection()[0]
        index = self.lb1.curselection()[0]

        # get the line's text

        ##seltext = lb1.get(index)
        seltext = self.lb1.get(index)

        self.master.destroy()

        # delete previous text in enter1
        enter1.delete(0, 50)
        ##        # now display the selected text
        enter1.insert(0, seltext)