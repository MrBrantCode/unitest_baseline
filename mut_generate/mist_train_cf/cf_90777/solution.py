"""
QUESTION:
Create a function `find_min_max` that takes a list of numbers as input and returns a tuple containing the minimum and maximum values from the list without using the built-in `min()` and `max()` functions. The list will have at least 5 numbers and may contain duplicates.
"""

def find_min_max(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    
    for num in numbers:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    
    return minimum, maximum