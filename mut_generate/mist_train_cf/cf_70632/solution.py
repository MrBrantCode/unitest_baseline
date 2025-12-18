"""
QUESTION:
Create a function called `polymorphism_example` that showcases the concept of polymorphism in object-oriented programming. The function should take in a list of shapes and calculate the total area. The shapes can be circles, rectangles, or triangles, each with their own implementation of the area calculation method. The function should use polymorphism to call the appropriate area calculation method for each shape without knowing the specific shape type at compile time.
"""

from math import pi

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

def polymorphism_example(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    return total_area