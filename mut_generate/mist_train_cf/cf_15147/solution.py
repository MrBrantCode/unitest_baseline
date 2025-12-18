"""
QUESTION:
Create a function called `find_max` that takes three integer parameters `num1`, `num2`, and `num3`. The function should return the maximum value among the three input numbers without using any built-in comparison or sorting functions/operators.
"""

def find_max(num1, num2, num3):
    # Comparing the numbers using if-else statements
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3