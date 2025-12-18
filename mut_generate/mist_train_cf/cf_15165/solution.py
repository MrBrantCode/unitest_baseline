"""
QUESTION:
Create a function named `check_numbers` that takes a list of numbers as input and returns `True` if the list contains at least one positive number, followed by at least one negative number, and then at least one zero, in this specific order. The function should return `False` otherwise.
"""

def check_numbers(numbers):
    positive = False
    negative = False
    zero = False
    
    for num in numbers:
        if num > 0 and not positive:
            positive = True
        elif num < 0 and positive and not negative:
            negative = True
        elif num == 0 and positive and negative:
            zero = True
    
    return positive and negative and zero