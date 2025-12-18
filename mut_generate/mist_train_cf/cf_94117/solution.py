"""
QUESTION:
Write a function named `extract_numbers` that takes a string as input. Using the re module, extract all the numbers greater than 5 from the string, which also contains at least one special character. The special characters can be any non-alphanumeric character. Return the extracted numbers as a list, sorted in descending order. If no numbers greater than 5 are found, return an empty list.
"""

import re

def extract_numbers(string):
    # Find all numbers in the string using regular expression
    numbers = re.findall(r'\d+', string)
    
    # Filter out numbers that are less than or equal to 5 and check if string contains a special character
    numbers_greater_than_5 = [int(num) for num in numbers if int(num) > 5 and not string.isalnum()]
    
    # Sort the numbers in descending order
    numbers_greater_than_5.sort(reverse=True)
    
    return numbers_greater_than_5