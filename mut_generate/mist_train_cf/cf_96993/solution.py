"""
QUESTION:
Write a function named `remove_even_numbers` that takes a list of integers as input, and returns the modified list with all even numbers removed. The input list may contain duplicate elements. Do not use any built-in functions or methods that directly delete elements from a list. The input list will always contain at least one element.
"""

def remove_even_numbers(lst):
    # Initialize an empty list to store the modified list
    result = []
    
    # Iterate through the input list
    for num in lst:
        # Check if the number is odd
        if num % 2 != 0:
            # Append the odd number to the result list
            result.append(num)
    
    # Return the modified list without even numbers
    return result