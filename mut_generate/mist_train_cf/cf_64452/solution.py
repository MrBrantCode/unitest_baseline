"""
QUESTION:
Create a function named `max_of_three` that takes three parameters of any numeric type, identifies their type, and returns the largest value among the three. The function should handle non-numeric inputs by returning a suitable error message. Ensure the function can accommodate integers and floats as input.
"""

def max_of_three(a, b, c):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        return max(a, b, c)
    else:
        return "Error: One or more inputs are not numeric."