# Default Values
def describe_pet(pet_name, animal_type = 'dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())

describe_pet(pet_name='Willie')
describe_pet('Willie')          #equivaluent way of calling a function

describe_pet('harry', 'hamster')
describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet(animal_type = 'hamster', pet_name = 'harry')


#Making an Argument Optional
def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:             #if middle is not empty
        full_name = first_name + middle_name + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'Lee')
print(musician)

#Using a function with a while loop
while True:
    print("\nPlease tell me your name: ")
    print("(Enter 'q' to quit at any time)")
    f_name = input("First name")
    if f_name == 'q':
        break
    l_name = input("last name")
    if l_name == 'q':
        break


#Returning a dictionary
def build_person(first_name, last_name, age = ''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age = 27)
print(musician)




#Modifying a list in a function
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        curren_design = unprinted_designs.pop()
        print("Printing model: " + curren_design)
        completed_models.append(curren_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
#Preventing a function from modifying a model
#   function_name(list_name[:])     ==> It's like copying a list and modifying it
#   print_models(unprinted_designs[:], completed_models)        ==> This won't modify the original list



#Mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
    print("\n Making a " + str(size)+ " -inch pizza with the following toppings: ")
    for topping in toppings:
        print("- "+ topping)
make_pizza(16, "pepperoni")
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



#Using Arbitrary keyword arguments
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_person('albert', 'einstein',location = 'princeton', field = 'physics')
print(user_profile)
