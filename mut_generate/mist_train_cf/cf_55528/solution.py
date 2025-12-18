"""
QUESTION:
Create a function named `sum_two_numbers` that takes two floating-point numbers as parameters and returns their sum with precision up to two decimal places. The function should not handle user input or validation. Write the rest of the program to handle user input, validate it to ensure the numbers are within the range -1000 to 1000, and handle non-numeric inputs by providing a custom error message.
"""

def sum_two_numbers(num1, num2):
    """This function sums two numbers with a precision of two 
       decimal places. It accepts float as inputs"""
    return round(num1 + num2, 2)