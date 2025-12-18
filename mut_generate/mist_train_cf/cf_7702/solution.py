"""
QUESTION:
Write a function `calculate_area` that takes the lengths of three sides of a triangle as input and returns the area of the triangle using Heron's formula. Additionally, implement a function `calculate_sqrt` to calculate the square root of a number without using any built-in mathematical functions or libraries. The `calculate_sqrt` function should be used to calculate the square root in `calculate_area`.
"""

def calculate_sqrt(num):
    """
    Calculate the square root of a number without using built-in mathematical functions.
    
    Args:
    num (float): The number to calculate the square root of.
    
    Returns:
    float: The square root of the number.
    """
    guess = num / 2
    while True:
        new_guess = (guess + num / guess) / 2
        if abs(new_guess - guess) < 0.0001:
            return new_guess
        guess = new_guess

def calculate_area(a, b, c):
    """
    Calculate the area of a triangle using Heron's formula.
    
    Args:
    a (float): The length of side a.
    b (float): The length of side b.
    c (float): The length of side c.
    
    Returns:
    float: The area of the triangle.
    """
    s = (a + b + c) / 2
    area = calculate_sqrt(s * (s - a) * (s - b) * (s - c))
    return area