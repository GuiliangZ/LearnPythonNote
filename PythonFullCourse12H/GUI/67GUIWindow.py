# Graphical User Interface

from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window_1 = Tk()   # instantiate an instance of a window
window_1.geometry("420x420")
window_1.title("Bro Code First GUI program")

# change the icon of the window to whatever picture you choose
# icon = PhotoImage(file = 'logo.png')
# window_1.iconphoto(True, icon)

#change the color of the window (hex color picker: https://www.google.com.hk/search?q=hex+color+picker&oq=hex+color+p&aqs=chrome.0.0i512j69i57j0i512l8.2723j0j7&sourceid=chrome&ie=UTF-8)
window_1.config(background="black")

window_1.mainloop()     #place window on computer screen, listen for events











