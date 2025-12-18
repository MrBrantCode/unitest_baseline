"""
QUESTION:
Write a Python function named `polymorphic_area` that calculates the area of different shapes using polymorphism. The function should take a list of shapes as an argument, where each shape is an instance of a class that inherits from a base `Shape` class. The `Shape` class should have a method `get_area` that returns the area of the shape. The function should return a list of the areas of all the shapes in the input list.

The `Shape` class and its subclasses should demonstrate encapsulation by keeping their implementation details private. The `polymorphic_area` function should be able to handle different types of shapes without knowing their specific class type.

The `Shape` class should have subclasses `Square` and `Circle`, where `Square` has a side length and `Circle` has a radius. The `get_area` method of each subclass should calculate the area of the shape according to its specific formula.
"""

class Shape:
    def __init__(self):
        self._area = 0

    def get_area(self):
        return self._area

class Square(Shape):
    def __init__(self, side):
        self._side = side
        self._area = self._side * self._side

    def get_area(self):
        return self._area

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self._radius = radius
        self._area = 3.14 * (self._radius ** 2)

    def get_area(self):
        return self._area

def polymorphic_area(shapes):
    areas = []
    for shape in shapes:
        areas.append(shape.get_area())
    return areas