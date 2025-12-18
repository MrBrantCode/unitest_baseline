"""
QUESTION:
Construct a function called "classify_number" that takes an integer as an argument and returns "positive", "negative", or "zero" based on its value. The function should return "positive" for values greater than 0, "negative" for values less than 0, and "zero" for values equal to 0. You are not allowed to use if-else statements or comparison operators (>, <, ==) in your implementation of the function.
"""

def classify_number(n):
    return ("zero", "positive", "negative")[int(n > 0) - int(n < 0)]