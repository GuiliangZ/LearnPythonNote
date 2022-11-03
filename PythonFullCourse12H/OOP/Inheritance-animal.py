#Inheritance        -- to recieve,derive or be left with
#A class can inherit something, usually attributes and methods from other class
#A class can have children and give whatever they own to their children
#Inherit from one common class
class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")
    
    def sleep(self):
        print("This animal is sleeping")

#Rabbit is the child class and the Animal is the parent class
#child class will inherit all the attributes and actions parent class has
class Rabbit(Animal):
    def run(self):
        print("This rabbit is running!")
class Fish(Animal):
    def swim(self):
        print("This fish is swiming!")
class Hawk(Animal):
    def fly(self):
        print("This Hawk can fly!")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()






