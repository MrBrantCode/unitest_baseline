"""
QUESTION:
Write a function `calculate_sum` that takes a string of numbers separated by commas and returns the sum of all the numbers. The string may contain negative numbers, floating-point numbers, and numbers enclosed in parentheses. There may be spaces between the numbers and commas. The function should ignore any invalid characters, such as letters or special symbols, and handle strings that contain multiple levels of nested parentheses.
"""

import re

def calculate_sum(numbers):
    numbers = numbers.replace(" ", "").replace("(", ",").replace(")", ",")
    numbers = re.sub("[^0-9.,()-]", "", numbers)
    numbers = numbers.split(",")
    total_sum = 0
    for number in numbers:
        try:
            total_sum += float(number)
        except ValueError:
            pass
    return total_sum