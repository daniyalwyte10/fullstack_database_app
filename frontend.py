from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index=ls1.curselection()[0]
    selected_tuple=ls1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


def view_text():
    ls1.delete(0, END)
    for row in backend.view():
        ls1.insert(END, row)


def search_text():
    ls1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        ls1.insert(END, row)


def add_text():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    ls1.delete(0, END)
    ls1.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_text():
    backend.delete(selected_tuple[0])


def update_text():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


window=Tk()
window.wm_title("BOOKSTORE")

l1=Label(window, text='Title')
l1.grid(row=0, column=0)

l2=Label(window, text='Author')
l2.grid(row=0, column=2)

l3=Label(window, text='Year')
l3.grid(row=1, column=0)

l4=Label(window, text='ISBN')
l4.grid(row=1, column=2)

title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window, textvariable=isbn_text)
e4.grid(row=1,column=3)

ls1=Listbox(window, height=6, width=35)
ls1.grid(row=2, column=0, rowspan=6, columnspan=2)

sc1=Scrollbar(window)
sc1.grid(row=2, column=2, rowspan=6)

ls1.configure(yscrollcommand=sc1.set)
sc1.configure(command=ls1.yview)

ls1.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(window, text='View All', width=13, command=view_text)
b1.grid(row=2, column=3)

b2=Button(window, text='Search Entry', width=13,command=search_text)
b2.grid(row=3, column=3)

b3=Button(window, text='Add Entry', width=13, command=add_text)
b3.grid(row=4, column=3)

b4=Button(window, text='Update Entry', width=13,command=update_text)
b4.grid(row=5, column=3)

b5=Button(window, text='Delete Entry', width=13, command=delete_text)
b5.grid(row=6, column=3)

b6=Button(window, text='Close', width=13,command=window.destroy)
b6.grid(row=7, column=3)


window.mainloop()