# Walrus operator aka assignment expression :=
# New to python 3.8
# Assigns values to variables as part of the a larger expression

# happy = True
# print(happy)

#print(happy := True)

'''
foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)

'''

#followed by the video but this code is not correct
#########!!!!!!!!! not correct code
foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)

print(''.join(foods))



















