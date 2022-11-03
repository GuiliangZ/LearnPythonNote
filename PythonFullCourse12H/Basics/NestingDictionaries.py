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



