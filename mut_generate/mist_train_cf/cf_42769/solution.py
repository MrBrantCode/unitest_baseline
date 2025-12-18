"""
QUESTION:
Implement a `Rectangle` class with the following methods: 
- `__init__(self, origin, length=0, width=0)`: Initializes the rectangle with its origin point and dimensions.
- `area(self)`: Returns the area of the rectangle.
- `perimeter(self)`: Returns the perimeter of the rectangle.
- `is_square(self)`: Returns True if the rectangle is a square, False otherwise.
- `__str__(self)`: Returns a string representation of the rectangle in the format "Rectangle: Origin at (x, y), Length: l, Width: w". 
The class should inherit from the `Forme` class and use its `__init__` method to initialize the origin point of the shape.
"""

def rectangle(origin, length=0, width=0):
    return f"Rectangle: Origin at ({origin[0]}, {origin[1]}), Length: {length}, Width: {width}"