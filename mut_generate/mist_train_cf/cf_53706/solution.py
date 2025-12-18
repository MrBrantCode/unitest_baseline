"""
QUESTION:
Write a function named `contains_complex` that checks if a given list contains at least one complex number. The function should iterate over the list, checking the type of each element, and return `True` as soon as it encounters a complex number; if no complex numbers are found after checking all elements, it should return `False`.
"""

def contains_complex(numbers):
    for num in numbers:
        if isinstance(num, complex):
            return True
    return False