"""
QUESTION:
Write a function `geometric_mean(list_of_numerals)` that calculates the geometric mean of a list of numerals. The function should return an error message if the list is empty or contains zero or negative numbers.
"""

from math import pow

def geometric_mean(list_of_numerals):
    # Error checking - check if list is empty
    if len(list_of_numerals) == 0:
        return "Error: The list is empty."

    # Error checking - check for zero or negative numbers in the list
    for number in list_of_numerals:
        if number <=0:
            return "Error: The list contains zero or negative numbers."

    # Calculate the geometric mean
    product = 1
    for number in list_of_numerals:
        product *= number

    geometric_mean = pow(product, 1.0/len(list_of_numerals))
    return geometric_mean