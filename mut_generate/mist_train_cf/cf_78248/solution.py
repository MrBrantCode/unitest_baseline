"""
QUESTION:
Write a function named `reverse_array` that takes a one-dimensional array as input and returns the reversed array without using any built-in array reversal functions or algorithms. The function should only utilize fundamental programming constructs such as loops, variables, and expression evaluation.
"""

def entrance(input_array):
    # Initialize start and end indexes
    start = 0
    end = len(input_array) - 1

    # Reverse the array elements
    while start < end:
        # Swap elements at start and end
        input_array[start], input_array[end] = input_array[end], input_array[start]
        # Move towards center
        start += 1
        end -= 1

    return input_array