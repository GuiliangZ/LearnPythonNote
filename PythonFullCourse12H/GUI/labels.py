from tkinter import *

#label = an area widget that holds text and/or an image within a window

window = Tk()

###########!!!!!!!!! cant figure why this code doesn't work
photo = PhotoImage(file = 'zxc.png')

label = Label(window, text = "Hello world", 
              font = ('Arial',40,'bold'), 
              fg = '#00FF00',
              bg = 'black',
              relief= SUNKEN,
              bd = 10,
              padx = 20,
              pady = 20,
              image = photo,
              compound = 'bottom')
#label.place(x = 100, y = 100)
label.pack()

window.mainloop()





