"""
QUESTION:
Create a class named `RegularPentagonalPrism` in Python with an initializer that takes two parameters, `side_length` and `height`, and includes two methods: `volume` to calculate the volume and `surface_area` to calculate the surface area of the prism. Assume the input values are valid (i.e., positive numbers).
"""

import math

def entrance(side_length, height):
    class RegularPentagonalPrism:
        def __init__(self, side_length, height):
            self.side_length = side_length
            self.height = height

        def volume(self):
            apothem = self.side_length / (2 * math.tan(math.pi / 5))
            area = 5 * self.side_length * apothem / 2
            return area * self.height

        def surface_area(self):
            apothem = self.side_length / (2 * math.tan(math.pi / 5))
            base_area = 5 * self.side_length * apothem / 2
            lateral_area = 5 * self.side_length * self.height
            return 2 * base_area + lateral_area

    prism = RegularPentagonalPrism(side_length, height)
    return prism.volume(), prism.surface_area()