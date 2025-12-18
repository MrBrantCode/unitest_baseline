"""
QUESTION:
Create a function called `classify_number` that takes a real number as input and returns a string indicating whether the number is "positive", "zero", or "negative". The function should handle both integer and floating-point numbers.
"""

def classify_number(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"