# Class - A blueprint for creating objects - custom data type

# class Car: # Instances and memory location
#     # Constructor - A special method that sets up attributes of a new instance
#     # called automatically whrn a new instance is created
#     def __init__(self): # Self is passed implicitly by the interpreter
#         print(f'Called __init__')
#         print(self)

# Main
# my_car = Car() # create a new instance of Car
# # my_car is now an object of class 'Car'
# your_car = Car() # Another Car object created
# print(my_car)
# print(your_car)

class Car:
    def __init__(self, make, model):
        # Create an attribute 'make' & copy the value of 'make' param into it
        self.make = make # dot notation - <object>.<attr/method>
        self.model = model 
    
    def start(self):
        print(f'{self.make} {self.model} started!')


# Main
my_car = Car('Toyota', 'Prius')
my_car.start()
your_car = Car('Ford', 'Ranger') 
# print(my_car.__dict__) # Useful during dev/debugging
your_car.start()