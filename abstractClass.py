from abc import ABC , abstractmethod
# you cannot create object for abstreact class
# class inheriting abstract class must override all abstrat methods
# if you want private variable use this __ before the varible (private = cannot access outside the class)
# __variable called Dunder variable

class Vehicals(ABC): #abstract class
    @abstractmethod #decorator
    def start(self):
        pass
    def stop(self):
        pass
    
class Bikes(Vehicals):
    color = None
    def start(self):
        print("You are buy a bike...")
        
class Cars(Vehicals):
    color = "Black"
    def start(self):
        print("You are buy a cars...")
        
        
bike1= Bikes()
bike1.start()

def setColor(car , color):
    car.color = color
    car.start() # duck typing (importance to methods than the objects)
    
car1 = Cars()
bike1 = Bikes()

setColor(bike1 , "Red") #passing Objects
setColor(car1 , "Blue")

print(car1.color)
print(bike1.color)

