# Shape base class with and area() method
# Subclases such as square, circle, triangle etc

# import math


# class Shape: # Defines an Abstract interface area()
#     def area(self): # area() method declares every Shape should have an area() method- hides how
#         pass

# class Circle(Shape): # 'Circle' implements area() method as required by 'Shape - Circle becomes a concrete class
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)
    
# # Main
# c1 = Circle(7)
# print(c1.area())

# c1 = Shape()
# print(c1.area()) # Returns None bc Shape is an abstraction

import math
from abc import ABC, abstractmethod # Abstract Base Class # Now Shape is enforced as abstract

class Shape(ABC): # Shape is now an abstract class 
    @abstractmethod # Decorator. Enforces every subclass to declare the area () method
    def area(self): 
        pass

class Circle(Shape): 
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
        
# Main
c1 = Circle(7)
print(c1.area())
r1 = Rectangle(7, 10)
print(r1.area())

