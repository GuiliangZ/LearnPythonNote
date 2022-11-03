class Car:

    #construct method -- constructor -- __init___
    #Thinking self as the name of the object that we working on

    #class variable is decleared inside the class but outside the constructor

    wheels = 4                   #class variable

    def __init__(self,make, model, year, color):
        self.make = make        #instance variable
        self.model = model      #instance variable
        self.year = year        #instance variable
        self.color = color      #instance variable

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")
