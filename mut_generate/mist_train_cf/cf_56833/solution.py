"""
QUESTION:
Create a class hierarchy with a base class `Polygon` that takes the number of sides as input and calculates internal angles. It should have methods to input and display sides, vertices, and angles. 

Derive three subclasses: `Triangle`, `Square`, and `RegularPolygon`, each inheriting from the `Polygon` class. 

- The `Triangle` class should calculate the area using the formula for a triangle given its sides.
- The `Square` class should calculate the area using the formula for a square given its side length.
- The `RegularPolygon` class should calculate the area using the formula for a regular polygon given its side length and number of sides.

Assume the math library is available for calculations. The input for sides and vertices can be any list of numbers and tuples of coordinates respectively. The internal angle calculation should be based on the number of sides of the polygon.
"""

from math import sin, pi, tan

def calculate_polygon_properties(num_sides):
    class Polygon:
        def __init__(self, num_sides):
            self.n = num_sides
            self.sides = [0 for i in range(num_sides)]
            self.vertices = [(0, 0) for i in range(num_sides)]
            self.angles = [self.calculate_internal_angle() for _ in range(num_sides)]  

        def input_sides(self, sides):
            self.sides = sides

        def input_vertices(self, vertices):
            self.vertices = vertices

        def calculate_internal_angle(self):
            return (self.n-2)*180/self.n

        def display(self):
            print("Number of sides:", self.n)
            print("Sides:", self.sides)
            print("Angles:", self.angles)
            print("Vertices:", self.vertices)

    class Triangle(Polygon):
        def __init__(self):
            Polygon.__init__(self, 3)
            
        def calculate_area(self):
            a, b, c = self.sides
            # calculate the semi-perimeter
            s = (a + b + c) / 2
            # calculate the area
            return (s*(s-a)*(s-b)*(s-c)) ** 0.5


    class Square(Polygon):
        def __init__(self):
            Polygon.__init__(self, 4)
            
        def calculate_area(self):
            side = self.sides[0]
            # calculate the area
            return side ** 2


    class RegularPolygon(Polygon):
        def __init__(self, num_sides):
            Polygon.__init__(self, num_sides)
            
        def calculate_area(self):
            side = self.sides[0]
            # Use the formula for the area of a regular polygon
            return (self.n * side**2) / (4 * tan(pi/self.n))

    return Polygon, Triangle, Square, RegularPolygon

Polygon, Triangle, Square, RegularPolygon = calculate_polygon_properties(5)