def hello():
    print("Hello")

hello()
#If print a function, it will display the memory address of that function
print(hello) 

hi = hello
print(hi)
hello()
hi()

say = print
say("Whoa! I can't believe this works! :O")













