"""
QUESTION:
Write a function named `count_digits` that takes an integer as input and returns the number of digits in the integer. The function should handle negative integers and return an error message if the input is not a valid integer. The solution should not use any built-in string or mathematical functions, and the time complexity should be O(log n), where n is the value of the input integer.
"""

def count_digits(num):
    if type(num) != int:
        return "Error: Invalid input"

    if num < 0:
        num = -num

    if num == 0:
        return 1

    count = 0
    while num > 0:
        num //= 10
        count += 1

    return count