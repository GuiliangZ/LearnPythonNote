# return statement = Functions send Python values/objects back to the caller.
#                   These values/objects are know as the function's return value

from unicodedata import name
from unittest import result


def multiply(number1,number2):
    return number1 * number2

x = multiply(6,8)
print(x)

# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional argument
#                       Python konws the names of the arguments that our function receives
def hello(first, middle, last):
    print("Hello " + first + " "+middle + " " + last)

hello(last ="code",middle = "Dude", first= "Bro" )

#Making an Argument optional
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:                     #Python interprets non-empty string as True
        full_name = first_name + middle_name + last_name
    else:
        full_name = first_name + last_name
    return full_name.title()




# nested functions calls = function calls inside other function calls
#                          innermost function calls are resolved first
#                           returned calue is used as argument for the next outer function
num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))

# scope =  the region that a variable is recognized
#           A variable is only available from inside the region it is created
#           A global and locally scoped versions of a variable can be created
#           Will first use a local version of the variable and then global
#           L = Local, E = Enclosing, G = Global, B = Built-in

name = "Bro"        #global scope(available inside & outside function)
def display_name():
    name = "code"   #local scope (available only inside this function)
    print(name)

display_name()
print(name)

# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of argument
def add(*args):
    sum = 0
    args = list(args)   #
    args[0] = 0
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4,5,6,7))

# **kwargs = parameter that will pack all arguments into a dictionary  (like args)
#            useful so that a function can accept a varying amount of keyword argument(kwarg)
def hello(**kwargs):
    #print("Hello "+ kwargs['first']+" "+ kwargs['last'])
    print("Hello", end = " ")
    for key, value in kwargs.items():
        print(value, end = " ")
hello(title = "Mr.", first = "Bro", middle = "Dudde",last = "code")

# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

#print("The " + animal + " jumped over the " + item)
print("The {0} jumped over the {1}".format(animal,item)) #positional argument
print("The {1} jumped over the {0}".format(animal,item)) #keyword argument
print("The {item1} jumped over the {animal1}".format(animal1 = "cow1",item1 = "moon1")) #keyword argument
text = "The {} jumped over the {}"
print(text.format(animal,item))
print("Hello, my name is {:10}. Nice to meet you.".format(name))
print("Hello, my name is {:<10}. Nice to meet you.".format(name))
print("Hello, my name is {:>10}. Nice to meet you.".format(name))
print("Hello, my name is {:^10}. Nice to meet you.".format(name))

number = 3.1415926
number2 = 10000
print("The number pi is {:.2f}".format(number))
print("The number pi is {:,}".format(number2))
print("The number pi is {:b}".format(number2))
print("The number pi is {:o}".format(number2)) #octal number
print("The number pi is {:X}".format(number2)) #Hexdecimal
print("The number pi is {:E}".format(number2)) #Scientific

# Random module -- pseudo-random numbers
import random 
x = random.randint(1,6)
y = random.random()
mylist = ['rock','paper','scissors']
z = random.choice(mylist)
card = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(card)
print(card)

# exception handling = events detected during execution that interrupt the flow of a program
try:
    numerator = int(input("Enter a number to a divide: "))
    denominator = int(input("Enter a number to a divide by: "))
    result = numerator / denominator
    #print(result)
except ZeroDivisionError as e:               #first catch specific exceptions
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong ;(")
else:                                          #if there's no exceptions occured
    print(round(result))
finally:                                    #whether or not catch an exception we will always execute any code that is in the finally code clause
    print("This will always execute")
