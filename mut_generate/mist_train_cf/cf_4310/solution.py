"""
QUESTION:
Write a function named `calculate_average` that takes a list as input. The function should find the first positive integer in the list, square it, and then calculate the sum of all elements in the list. It should then return the rounded average of the squared integer and the sum. The function should ignore non-integer elements in the list and return the result rounded to the nearest whole number.
"""

import math

def entrance(list):
    # Find the first positive integer element
    for num in list:
        if isinstance(num, int) and num > 0:
            positive_integer = num
            break
    
    # Square the positive integer element
    squared_element = positive_integer ** 2
    
    # Calculate the sum of all elements, ignoring non-integer values
    sum_of_elements = sum(num for num in list if isinstance(num, int))
    
    # Calculate the average of squared element and sum
    average = (squared_element + sum_of_elements) / 2
    
    # Round the average to the nearest whole number
    rounded_average = round(average)
    
    # Return the rounded average
    return rounded_average