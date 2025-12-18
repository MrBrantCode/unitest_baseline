"""
QUESTION:
Create a function called `smallest_odd_number` that takes a list of integers as input, ignoring any instances of zero. Without using built-in functions, the function should return the smallest odd integer in the list. If no odd numbers are found, it should return `None`.
"""

def smallest_odd_number(lst: list):
    smallest = None
    for num in lst:
        if num == 0:
            continue
        elif num % 2 != 0:
            if smallest is None or num < smallest:
                smallest = num
    return smallest