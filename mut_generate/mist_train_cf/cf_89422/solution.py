"""
QUESTION:
Write a function `count_digits(num)` that takes an integer as input and returns the number of digits in the integer. The function should handle negative integers and return an error message if the input is not a valid integer. The function should not use any built-in string or mathematical functions and should have a time complexity of O(log n), where n is the value of the input integer.
"""

def count_digits(num):
    # Check if the input is a valid integer
    if type(num) != int:
        return "Error: Invalid input"

    # Handle negative integers
    if num < 0:
        num = -num

    # Handle the special case when num is 0
    if num == 0:
        return 1

    # Count the number of digits using log base 10
    count = 0
    while num > 0:
        num //= 10
        count += 1

    return count