# button = you click it, then it does stuff


from tkinter import *
count = 0

def click():
    global count
    count += 1
    print(count)
    print("You clicked the button!")



window =Tk()

######### !!!!!!!! import image thing never worked for me!
#photo = PhotoImage(file = 'download.png')

button = Button(window,
                text = "click me",
                command = click,         #use click not click(), this is called "callback"
                font = ("Comic Sans", 30),
                fg = "#00FF00",
                bg = "black",
                activeforeground="#00FF00",
                activebackground= "black",)
#                state = DISABLED,)
#                image = photo,
#                compound = 'bottom')   

button.pack()


window.mainloop()


