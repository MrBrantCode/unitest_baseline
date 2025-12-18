"""
QUESTION:
Write a function `process_input` that takes user input, validates it as an integer, and returns the integer and a boolean indicating success. If the input cannot be converted to an integer, return an error message and False. Use this function to capture and validate 15 integers from user input. Then, calculate the median without using any sorting algorithms, built-in functions, comparison operators, or conditional checks. Handle cases for both odd and even sets of numbers and provide an error message for invalid input data types.
"""

def process_input(user_input):
    try:
        # Attempt to make the input into an integer
        int_input = int(user_input)
        return int_input, True
    except:
        return None, False