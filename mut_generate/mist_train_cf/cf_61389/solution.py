"""
QUESTION:
Write a function `right_angle_triangle(a, b, c)` that takes the lengths of three sides of a triangle as input and returns `True` if the sides form a right-angled triangle and `False` otherwise. The function should use the Pythagorean theorem to determine if the triangle is right-angled. The input sides may be in any order, and the function should work correctly regardless of their order.
"""

def right_angle_triangle(a, b, c):
    # First, sort a, b, and c in ascending order
    a, b, c = sorted([a, b, c])
    
    # The theorem defined by Pythagoras for a right-angled triangle states that the square of the hypotenuse (longest side) 
    # is equal to the sum of the squares of the other two sides
    # Hence we can use this theorem to verify if the triangle is right-angled or not
    return c**2 == a**2 + b**2