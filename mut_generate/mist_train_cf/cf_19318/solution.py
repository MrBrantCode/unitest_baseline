"""
QUESTION:
Write a function classify_number() that takes an integer as input and returns a string indicating whether the number is positive, negative, or zero, and whether it is even or odd.
"""

def classify_number(n):
    """Returns a string indicating whether the number is positive, negative, or zero, and whether it is even or odd."""
    
    if n == 0:
        return "zero"
    elif n > 0:
        return "positive" if n % 2 == 0 else "positive even"
    else:
        return "negative" if n % 2 == 0 else "negative odd"