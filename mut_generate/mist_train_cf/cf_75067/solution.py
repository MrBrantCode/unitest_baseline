"""
QUESTION:
Create a function named `squares_dictionary` that takes a list of numbers as input, returns a dictionary where the keys are the input numbers and the values are their squares, and handles non-numeric input.
"""

def squares_dictionary(numbers):
    try:
        return {num: num*num for num in numbers}
    except TypeError:
        print("Error: Non-numeric input")