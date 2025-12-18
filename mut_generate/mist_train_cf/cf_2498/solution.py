"""
QUESTION:
Create a function `absolute_difference(num1, num2)` that takes two integers as input and returns the absolute difference between them, without using any built-in absolute value functions or methods. Ensure that the first number is greater than or equal to the second number, and handle cases where the input numbers are negative. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

def absolute_difference(num1, num2):
    # Swap the numbers if the first number is smaller
    if num1 < num2:
        num1, num2 = num2, num1

    # Subtract the numbers and get the absolute difference
    result = num1 - num2
    if result < 0:
        result *= -1
    return result