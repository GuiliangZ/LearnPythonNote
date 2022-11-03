#String
#"\t" - add a tab to the text
#"\n" - add a newline in a string
#"string.rstrip()
# string.lstrip()
# string.strip() - look for whitespace on right and left side of the string and eliminate all the whitespace"
# string.title() - capitalize the first letter of the string value
print("Language: \n\tPython\n\tC\n\tJavaScript")


#Loop Control statements = change a loops execution from its normal sequence
#Break = used to terminate the loop entirely
#Continue = skips to the next iteration of the loop 
#Pass = Does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end = "")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)


#List = used to store multiple items in a single variable; dynamic
#Sortable. Item always started with the number starting with 0. Add items using .append
foods = ["pizza","hamburgers","hotdog","spaghetti","pudding"]
foods[0] = "sushi"
foods.append("ice cream")       #add new element to a list
foods.remove("hotdog")          #remove specific element by value
foods.pop()                     #remove last element, 
variable = foods.pop()             #can store the value in a variable and use it
foods.pop(0)                    #pop items from any position in a list
foods.insert(0,"cake")          #insert element to a specific location
del foods[0]                      #removing an item using del statement
foods.sort()                    #change the order of element by alphabetical order permenantly
foods.sort(reverse = True)      #sort the list in reverse alphabetical order
sorted(foods)                   # sort temporarily
foods.reverse()                 #reverse the order of the list permanently
len(foods)                      #find the length of a list
foods.clear()
print(foods[4])
for x in foods:
    print(x)

#Looping through entire list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:     #Use singular and plural names, magician is a temporary variable
    print(magician)

#Making numerical lists
for value in range(1,5):
    print(value)            #Only print: 1,2,3,4    -- Off by one behavior
even_numbers = list(range(2,11,2))      #tells python start from 2, end with 11, and add 2 to that value
#make a list of first 10 square numbers
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
    #squares.append(value**2)
#Simple statistic with a list numbers
digits = list(range(1,11))
maxNum = max(digits)
minNum = min(digits)
sumNum = sum(digits)
#List Comprehension
Squares = [value**2 for value in range(1,11)]

#Working with Part of a list: can work with specific group of items in a list(slice)
#To make a slice, you specify the index of the first and last elements you want to work with
#To use a range() function, Python stops one item before the second index you sepcify
#The lower index of a slice is inclusive and the upper index is exclusive. 
#And leaving out the lower index starts the slice at 0, while leaving out the upper index ends the slice at the end of the list.
Players = ['Charles','martina','michael','florence','eli']
print(Players[0:3])         #['Charles','martina','michael'] (also a list)
print(Players[1:4])         #['martina','michael','florence']
print(Players[:4])         #['Charles','martina','michael','florence']
print(Players[2:])          #['michael','florence','eli']
print(Players[-3:])         #['michael','florence','eli']
#Looping through a slice
for player in Players[:3]:
    print(Players.title())
#Copying a list
friend_foods = foods[:]     #copying the whole list 


#2D list = a list of lists
drinks = ["coffee", "soda", "tea"]
dinner = ["chicken", "beef", "lamp"]
dessert = ["cake","ice cream"]
food = [drinks,dinner,dessert]
print(food)
print(food[0])
print(food[0][1])
print(food[1][2])


#tuple = collection which is ordered and unchangeable       ==> if you want to change a tuple, you have change all the elements in the tuple
#        used to group together related data
students = ("Bro",21,"male")
print(students.count("Bro"))     #how many times bro accured
print(students.index("male"))


dimensions = (200,50)
print(dimensions)
dimensions = (250,100)
print(dimensions)
#dimensions[0] = 250            #Error == > cause can't change single elements in the tuple 

for student in students:               #x is automatic index for tuple/list
    print(x)

if "Bro" in students:            #
    print("Bro is here!")

#Tuple unpacking
#With tuple, the () is optional
dimensions = 50,42,100
height, length, width = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))




#set = collection which is unordered, unindexed. No duplicate value
#set is faster than a list if you need to check to see 
# if something is within a set compared to a list and they don't allow duplicate values
#Order in which items can be inconsistent. Mutable. add items with .add
utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup"}

for x in dishes:
    print(x)

utensils.update(dishes)
for x in utensils:
    print(x)

utensils.add("napkin")
utensils.remove("fork")
#utensils.clear()

for x in utensils: 
    print(x)

dinner_table = utensils.union(dishes)
for x in dinner_table: 
    print(x)

print(utensils.difference(dishes))
print(dishes.difference(utensils))
print(utensils.intersection(dishes)) #common in two sets




#dictionary = A changable, unordered collection of unique key:value pairs
#                Fast because they use hashing, allow us to access a value quickly
#Each items contain two part. Order in which items appear can be inconsistent. can be nested
capitals = {'USA': 'Wshington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
#capitals.clear()
#print(capitals['Russia'])
print(capitals.get('Germany'))
print(capitals.get('China'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
for key,value in capitals.items():
    print(key, value)

#Adding new key-value pairs
alien = {'color':'green','point': 5}
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)                ##{'color':'green','point': 5,'y_position':25,'x_position',0}

#Starting with an Empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['point'] = 5
print(alien_0)

#Removing key-value pairs
alien_0 = {'color': 'green','point':5}
del alien_0['point']

#Looping through All key-value pairs
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
for key, value in user_0.items():   ##.items() ==> loop through both key and value, doesn't matter the sequence
    print("\nkey: " + key)
    print("Value: " + value)

for name in user_0.keys():          ## .keys() ==> loop through only keys
    print(name.title())

for language in user_0.values():    ## .values() ==> loop through only values 
    print(language.title())




#Nesting Dictionaries
#A list of Dictionaries
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yello'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)

print("Total number of aliens: " + str(len(aliens)))


#A list in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + " -crust pizza"+
        "with the following toppings: ")

for topping in pizza['toppings']:
    print("\t" + topping)


#A dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for username, user_info in users.items():
    print("\n Username: "+username)
    full_name = user_info['first'] + " "+ user_info['last']
    location = user_info['location']

    print("\t Full name: "+ full_name.title())
    print("\tlocation: "+ location.title())


#Using a while loop with lists and dictionaries

#moving items from one list to another
unconfirmed_users = ['Alice','Brain','candace']
confirmed_users = []

while unconfirmed_users:            #Python evaluate non-empty list as true
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user)
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#Removing all instance of specific values from a list
pets = ['dog','cat','dog','goldfish','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)


#Filing a dictionary with user input
responses = {}
polling_active = True      #set a flag to indicate that polling is active.
while polling_active:
    name = input("\nWhat is your name?")
    response_1 = input("Which mountain would you like to climb?")

    responses[name] = response_1

    repeat = input("Is there another person need to respond? yes/no  ")
    if repeat == 'no':
        polling_active = False

print("Poll Results")
for name, response_1  in responses.items():
    print(name + " would like to climb "+ response_1)





#index operator [] = gives access to a sequence's  element (str, list, tuples)
name = "bro COde!"
print(name)
if (name[0].islower()):
    name = name.capitalize()
first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]           #last indexing is -1
SecondTolast_character = name[-2]   #second to last indexing is -2
print(first_name)
print(last_name)
print(last_character)
print(SecondTolast_character)