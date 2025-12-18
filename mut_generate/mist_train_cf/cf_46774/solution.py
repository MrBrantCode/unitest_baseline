"""
QUESTION:
Write a recursive function called `find_min` that takes a list of arbitrarily nested lists of numbers and returns the smallest integer value present in the list. The function should ignore non-integer data types. If no integer is present in the list, the function should return `None`.
"""

def find_min(data, smallest=None):
    for item in data:
        if isinstance(item, list):
            smallest = find_min(item, smallest)
        elif isinstance(item, int):
            if smallest is None or item < smallest:
                smallest = item  
    return smallest