"""
QUESTION:
Create a function `process_number(num)` that takes a number as input and returns the square of the number if it is positive, the cube if it is negative, and zero if it is zero. Use nested ternary operators to achieve this behavior within the function. Then, utilize list comprehension to process a list of numbers and print the resulting list of processed values.
"""

def process_number(num):
    return num**2 if num > 0 else (num**3 if num < 0 else 0)