#file detection
from cgitb import text
import os
#checking whether a file exist somewhere in the computer
path = "/Users/zheng/Desktop/Code/Python/LearnPython"
if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist!")

#
# read the content in a file 
try:
    with open('test.rt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

#
# write the content in a file
text = "Have a nice day! See ya"
with open('test.rtf','a') as file:
    file.write(text)


#copy files in python
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata(file's creation and modification times)
import shutil
shutil.copyfile('test.rtf','/Users/zheng/Desktop/copy.rtf') #source,destination


#move files using python
import os
source = "test.rtf"
destination = "/Users/zheng/Desktop/test.rtf"
try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source + "was moved")
except FileNotFoundError:
    print(source + " was not found")


#Delete file using python
# os.remove(path)           #delete a file
# os.rmdir(path)            #delete an empty directory
# shutil.rmtree(path)       #delete a directory containing files
try:
    os.remove('copy.rtf')
except FileNotFoundError:
    print("That file was not found")




