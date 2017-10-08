from tkinter import *
from backend02 import Database

database=Database()

class Window(object):
    def __init__(self,window):
        self.window=window
        self.window.wm_title("Book Store")

        l1=Label(self.window,text="Title")
        l1.grid(row=0,column=0)
        l1=Label(self.window,text="Author")
        l1.grid(row=0,column=2)
        l1=Label(self.window,text="Year")
        l1.grid(row=1,column=0)
        l1=Label(self.window,text="ISBN")
        l1.grid(row=1,column=2)

        e1_title = StringVar()
        e1=Entry(self.window,textvariable=e1_title)
        e1.grid(row=0,column=1)
        e1_author = StringVar()
        e1=Entry(self.window,textvariable=e1_author)
        e1.grid(row=0,column=3)
        e1_year = StringVar()
        e1=Entry(self.window,textvariable=e1_year)
        e1.grid(row=1,column=1)
        e1_ISBN = StringVar()
        e1=Entry(self.window,textvariable=e1_ISBN)
        e1.grid(row=1,column=3)

        self.list1=Listbox(self.window, height=6, width=35)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)
        self.list1.bind('<<listboxSelect>>',self.get_selected_row)
        sb1=Scrollbar(self.window)
        sb1.grid(row=2,column=2,rowspan=6)
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        b1=Button(self.window,text="View All",width=12,command=self.view_command)
        b1.grid(row=2,column=3)
        b1=Button(self.window,text="Search Entry",width=12,command=self.search_command)
        b1.grid(row=3,column=3)
        b1=Button(self.window,text="Add Entry",width=12,command=self.add_command)
        b1.grid(row=4,column=3)
        b1=Button(self.window,text="Update",width=12,command=self.update_command)
        b1.grid(row=5,column=3)
        b1=Button(self.window,text="Delete",width=12,command=self.delete_command)
        b1.grid(row=6,column=3)
        b1=Button(self.window,text="Close",width=12,command=self.window.destroy)
        b1.grid(row=7,column=3)


    def get_selected_row(self,event):
        global selected_tuple
        index=self.list1.curselection()[0]
        selected_tuple=self.list1.get(index)

    def view_command(self):
        self.list1.delete(0,END)
        for row in database.viewAll():
            self.list1.insert(END,row)

    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(e1_title.get(),e1_author.get(),e1_year.get(),e1_ISBN.get()):
            self.list1.insert(END,row)

    def add_command(self):
        database.insert(e1_title.get(),e1_author.get(),e1_year.get(),e1_ISBN.get())
        list1.delete(0,END)
        list1.insert(END,(e1_title.get(),e1_author.get(),e1_year.get(),e1_ISBN.get()))

    def delete_command(self):
       print("Delete")
    #    Database.delete(selected_tuple[0])

    def update_command(self):
        print("update")

window=Tk()
Window(window)

window.mainloop()
