"""
QUESTION:
Create a function called `find_min_max` that takes a list of numbers as input. The function should iterate over the list to find the minimum and maximum numbers. The minimum and maximum numbers should be initialized with a value that ensures any number in the list will be smaller or larger. The function should return the minimum and maximum numbers as a tuple. The function should not use the built-in `min` and `max` functions.
"""

def find_min_max(numbers):
    min_number = float('inf')
    max_number = float('-inf')
    
    for number in numbers:
        if number < min_number:
            min_number = number
        if number > max_number:
            max_number = number

    return min_number, max_number