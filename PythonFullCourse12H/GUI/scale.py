from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+" degree C")

window = Tk()

scale = Scale(window, 
              from_ = 100, 
              to = 0,
              length = 600,
              orient= VERTICAL, #orientation of scale
              font = ('Consolas', 20),
              tickinterval=10,  #adds numeric indicators for value
              showvalue=0,      #hide current value
              resolution=5,
              troughcolor='#69EAFF',
              fg= '#FF1C00',
              bg = '#111111'
              )

scale.set((scale['from'] - scale['to'])/2 + scale['to'])    #always put the cursor to the middle
scale.pack()

'''
hotImage = PhotoImage(file = 'hot.png')
hotLabel = Label(image = hotImage)
hotLabel.pack()

coldImage = PhotoImage(file = 'cold.png')
coldLabel = Label(image = coldImage)
coldLabel.pack()

'''

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()






