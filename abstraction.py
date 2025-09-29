# Shape base class with and area() method
# Subclases such as square, circle, triangle etc
import math


class Shape: # Defines an Abstract interface area()
    def area(self): # area() method declares every Shape should have an area() method- hides how
        pass

class Circle(Shape): # 'Circle' implements area() method as required by 'Shape - Circle becomes a concrete clas
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
# Main
c1 = Circle(7)
print(c1.area())
