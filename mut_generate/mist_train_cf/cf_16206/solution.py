"""
QUESTION:
Extract all numbers greater than 5 from a given string that contains at least one special character, and return them as a sorted list in descending order. The function name should be `extract_numbers` and it should take one argument `string`. The input string can be of any length and may contain multiple occurrences of special characters, which are any non-alphanumeric characters.
"""

import re

def extract_numbers(string):
    # Check if string contains at least one special character
    if not re.search(r'[^A-Za-z0-9]', string):
        return []
    
    # Find all numbers in the string using regular expression
    numbers = re.findall(r'\d+', string)
    
    # Filter out numbers that are less than or equal to 5
    numbers_greater_than_5 = [int(num) for num in numbers if int(num) > 5]
    
    # Sort the numbers in descending order
    numbers_greater_than_5.sort(reverse=True)
    
    return numbers_greater_than_5