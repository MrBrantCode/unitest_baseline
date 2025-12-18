"""
QUESTION:
Write a function `check_numbers(x, y)` that takes two integers as input and checks if they are both within the range of -1000 to 1000, if x is a multiple of 3, and if y is a multiple of 5. If these conditions are met, use bitwise operators to determine if both numbers are even. If they are even, return "Both even". If they are not both even, return "Not both even". If the initial conditions are not met, return "Out of range".
"""

def check_numbers(x, y):
    """
    Checks if two integers are within the range of -1000 to 1000, 
    if x is a multiple of 3, and if y is a multiple of 5. 
    Then, uses bitwise operators to determine if both numbers are even.

    Args:
        x (int): The first integer.
        y (int): The second integer.

    Returns:
        str: "Both even" if both numbers are even, "Not both even" if they are not both even, 
             and "Out of range" if the initial conditions are not met.
    """

    # Check if numbers are within range, x is a multiple of 3, and y is a multiple of 5
    if -1000 <= x <= 1000 and -1000 <= y <= 1000 and x % 3 == 0 and y % 5 == 0:
        # Use bitwise operators to check if both numbers are even
        if (x & 1) == 0 and (y & 1) == 0:
            return "Both even"
        else:
            return "Not both even"
    else:
        return "Out of range"