"""
QUESTION:
Write a function `area_and_isosceles_check(side1, side2, base)` that calculates the area of a triangle given its side lengths using Heron's formula and checks if the triangle is isosceles. The side lengths are floating point numbers between 1 and 50 inclusive, up to 2 decimal places. The function should handle the case where the given sides cannot form a triangle and return an error message.
"""

def area_and_isosceles_check(side1, side2, base):
    """
    Function to calculate the area of a triangle based on side lengths
    and check if the triangle is isosceles.
    """
    # validations
    if not(1 <= side1 <= 50) or not(1 <= side2 <= 50) or not(1 <= base <= 50):
        return "Invalid input: All sides should be between 1 and 50"

    # Check if the given sides can form a triangle
    if not(side1 + side2 > base and side1 + base > side2 and side2 + base > side1): 
        return "Invalid input: These sides can't form a triangle"

    # Check if the triangle is isosceles
    is_isosceles = side1 == side2 or side2 == base or base == side1

    # calculate semi-perimeter
    s = (side1 + side2 + base) / 2

    # calculate area using Heron's formula
    area = (s*(s-side1)*(s-side2)*(s-base)) ** 0.5

    return area, is_isosceles