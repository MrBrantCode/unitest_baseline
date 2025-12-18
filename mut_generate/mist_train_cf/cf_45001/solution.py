"""
QUESTION:
Write a function named `generate_nums` that takes an integer limit as input and generates all standard base-10 integers from 0 up to but not including the given limit. The limit should be a positive integer power of ten. The function should handle user input errors and return a list of generated numbers.
"""

def generate_nums(limit):
    if isinstance(limit, int) and limit > 0 and len(str(limit)) == len(str(10 ** (len(str(limit)) - 1))):
        return list(range(limit))
    else:
        return "Error: Please enter a positive integer power of ten."