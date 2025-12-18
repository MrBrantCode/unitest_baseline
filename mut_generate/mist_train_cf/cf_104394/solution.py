"""
QUESTION:
Create a function called `sum_of_squares` that takes two parameters: a list of numbers and an exponent. The function should calculate the sum of each number in the list raised to the power of the given exponent. If any negative number is present in the list, the function should return the error message "Error: Negative numbers are not allowed." Otherwise, it should return the calculated sum.
"""

def sum_of_squares(numbers, exponent):
    # Check if any negative number is present in the list
    if any(num < 0 for num in numbers):
        return "Error: Negative numbers are not allowed."
    
    # Calculate the sum of squares
    sum_of_squares = sum(num**exponent for num in numbers)
    return sum_of_squares