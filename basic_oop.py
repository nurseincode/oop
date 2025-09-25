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

# class Car:
#     def __init__(self, make, model):
#         # Create an attribute 'make' & copy the value of 'make' param into it
#         self.make = make # dot notation - <object>.<attr/method>
#         self.model = model 

    
#     def start(self):
#         print(f'{self.make} {self.model} started!')
    
#     def __str__(self):
#         return(f'This is {self.make} {self.model}') # return a readable string describing the object


# # Main
# my_car = Car('Toyota', 'Prius')
# # my_car.start()
# your_car = Car('Ford', 'Ranger') 
# # print(my_car.__dict__) # Useful during dev/debugging
# print(your_car)
# # print(my_car.display())
# # your_car.start()
# # print(my_car.make) # Accessing attributes, attrs not private by default
# # print(my_car.model)


class Car:
    def __init__(self, make, model):
        # Dunder makes the attribute private
        self.__make = make 
        self.model = model 

    
    def start(self):
        print(f'{self.__make} {self.model} started!')
    
    def __str__(self):
        return(f'This is {self.__make} {self.model}')


# Main
my_car = Car('Toyota', 'Prius')
# my_car.start()
# your_car = Car('Ford', 'Ranger') 
print(my_car.__make)

