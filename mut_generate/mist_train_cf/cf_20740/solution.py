"""
QUESTION:
Implement a function compare_numbers(num1, num2) that compares the absolute values of two numbers and returns 1 if num1 is greater, -1 if num1 is less, and 0 if they are equal. The function should only use bitwise operations and logical operators, and it should have a time complexity of O(1).
"""

def compare_numbers(num1, num2):
    # Get the absolute values of the numbers
    abs_num1 = (num1 ^ (num1 >> 31)) - (num1 >> 31)
    abs_num2 = (num2 ^ (num2 >> 31)) - (num2 >> 31)

    # Check if num1 is greater than num2
    if abs_num1 > abs_num2:
        return 1
    elif abs_num1 < abs_num2:
        return -1
    else:
        return 0