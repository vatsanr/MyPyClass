from tkinter import *
import backend01 as backend


def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)

def view_command():
    list1.delete(0,END)
    for row in backend.viewAll():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(e1_title.get(),e1_author.get(),e1_year.get(),e1_ISBN.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(e1_title.get(),e1_author.get(),e1_year.get(),e1_ISBN.get())
    list1.delete(0,END)
    list1.insert(END,(e1_title.get(),e1_author.get(),e1_year.get(),e1_ISBN.get()))

def delete_command():
   print("Delete")
#    backend.delete(selected_tuple[0])

def update_command():
    print("update")

window = Tk()
window.wm_title('Book Store')

l1=Label(window,text="Title")
l1.grid(row=0,column=0)
l1=Label(window,text="Author")
l1.grid(row=0,column=2)
l1=Label(window,text="Year")
l1.grid(row=1,column=0)
l1=Label(window,text="ISBN")
l1.grid(row=1,column=2)

e1_title = StringVar()
e1=Entry(window,textvariable=e1_title)
e1.grid(row=0,column=1)
e1_author = StringVar()
e1=Entry(window,textvariable=e1_author)
e1.grid(row=0,column=3)
e1_year = StringVar()
e1=Entry(window,textvariable=e1_year)
e1.grid(row=1,column=1)
e1_ISBN = StringVar()
e1=Entry(window,textvariable=e1_ISBN)
e1.grid(row=1,column=3)

list1=Listbox(window, height=6, width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)
list1.bind('<<listboxSelect>>',get_selected_row)
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)
b1=Button(window,text="Search Entry",width=12,command=search_command)
b1.grid(row=3,column=3)
b1=Button(window,text="Add Entry",width=12,command=add_command)
b1.grid(row=4,column=3)
b1=Button(window,text="Update",width=12,command=update_command)
b1.grid(row=5,column=3)
b1=Button(window,text="Delete",width=12,command=delete_command)
b1.grid(row=6,column=3)
b1=Button(window,text="Close",width=12,command=window.destroy)
b1.grid(row=7,column=3)




window.mainloop()
