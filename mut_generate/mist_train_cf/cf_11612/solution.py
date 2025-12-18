"""
QUESTION:
Implement a function `calculate_difference(num1, num2)` that takes two numbers as parameters. Calculate the difference between `num1` and `num2` only if `num1` is larger than `num2`. If `num1` is smaller or equal to `num2`, return "Difference cannot be calculated." If the difference can be evenly divided by 2, return the result divided by 2. If the difference cannot be evenly divided by 2, return the result multiplied by 2.
"""

def calculate_difference(num1, num2):
    if num1 <= num2:
        return "Difference cannot be calculated."
    
    difference = num1 - num2
    
    if difference % 2 == 0:
        return difference // 2
    else:
        return difference * 2