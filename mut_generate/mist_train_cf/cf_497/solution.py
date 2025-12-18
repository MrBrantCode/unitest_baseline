"""
QUESTION:
Write a function called `calculate_sum` that takes a string of numbers separated by commas as input and returns the sum of all the numbers. The string may contain negative numbers, floating-point numbers, and numbers enclosed in parentheses. There may be spaces between the numbers and commas, and the string may contain invalid characters, such as letters or special symbols, which should be ignored. The function should also handle strings that contain multiple levels of nested parentheses.
"""

import re

def calculate_sum(numbers):
    # Remove spaces from the string
    numbers = numbers.replace(" ", "")
    
    # Remove invalid characters from the string
    numbers = re.sub("[^0-9.,()-]", "", numbers)
    
    # Replace parentheses with commas to split the string into numbers
    numbers = numbers.replace("(", ",").replace(")", ",")
    
    # Split the string into a list of numbers
    numbers = numbers.split(",")
    
    # Initialize the sum
    total_sum = 0
    
    # Iterate over each number
    for number in numbers:
        try:
            # Convert the number to float and add it to the sum
            total_sum += float(number)
        except ValueError:
            # Ignore invalid numbers
            pass
    
    return total_sum