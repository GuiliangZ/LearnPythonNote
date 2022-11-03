#listbox = A listing of selectable text items within it's own container

from tkinter import *

from numpy import insert

def submit():
    food = []
    print("You have ordered: ")
    for index in listbox.curselection():
        food.insert(insert,listbox.get(index))

    for index in food:
           
    print(listbox.get(listbox.curselection()))

def add():
    listbox.config(height = listbox.size()) 
    listbox.insert(listbox.size(), entryBox.get())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height = listbox.size())


window = Tk()

listbox = Listbox(window,
                bg = "#f7ffde",
                font = ("Constantia",35),
                width = 12,
                    )

listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height = listbox.size())            #use config to change

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text="submit",command=submit)
submitButton.pack()

addButton = Button(window,text="add",command=add)
addButton.pack()

deleteButton = Button(window,text="delete",command=delete)
deleteButton.pack()

window.mainloop()







