#Abstract class = advantages: Prevents a user from creating an object of that class
#                             +Compels a user to override abstract methods in a child class
# A form of check and balances
# template, gost class, ideal, not real class


#abstract class = a class which contains one or more abstract methods
#abstract method = a method that has a declaration but does not have an implementation

#Create abstract class ==> abc stands for abstract based class

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod         #make sure that the child class have those methods ==> check and balance
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("You stopped the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("You stopped the motorcycle")

#vehicle = Vehicle()         #cannot give this class a physical form, or physical manifestation(Cannot be implemented)
car = Car()
motorcycle = Motorcycle()

#vehicle.go()        #To prevent the user to use this method, because it's not properly setup yet
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()












