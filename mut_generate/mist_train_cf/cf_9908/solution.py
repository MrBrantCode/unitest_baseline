"""
QUESTION:
Write a function named `reverse_list` that takes a list of integers as input and returns a new list with the same elements in reverse order. Do not use any built-in list manipulation functions or methods, such as `reverse()`. Implement the function using only basic programming constructs like loops and conditional statements. The input list can contain any number of elements.
"""

def reverse_list(input_list):
    # Initialize an empty list to store the reversed elements
    reversed_list = []
    
    # Iterate over the elements of the original list in reverse order
    for i in range(len(input_list) - 1, -1, -1):
        # Append each element to the reversed list
        reversed_list.append(input_list[i])
    
    # Return the reversed list
    return reversed_list