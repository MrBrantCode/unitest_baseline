"""
QUESTION:
Design a function named `find_smallest_even` that takes a list of integers as input and returns the smallest even number in the list along with its index(es) if it exists. If no even number is found, the function should return "No even number found!". The function should also handle errors for non-list inputs and non-integer values in the list, returning an error message in these cases.
"""

def find_smallest_even(lst):
    # Check if the input is a list
    if type(lst) is not list:
        return "Error: The provided input is not a list!"

    smallest_even = float('inf')
    smallest_even_indices = []

    for i in range(len(lst)):
        # Check if the element in the list is an integer
        if type(lst[i]) is not int:
            return "Error: List contains non-integer values!"
        
        # Check if the number is even and smaller than the current smallest even number
        if lst[i] % 2 == 0 and lst[i] < smallest_even:
            smallest_even = lst[i]
            smallest_even_indices = [i]   # Reset the list of indices
        elif lst[i] == smallest_even:
            smallest_even_indices.append(i)   # Add the index to the list

    # Check if any even number was found
    if smallest_even == float('inf'):
        return "No even number found!"
    else:
        return smallest_even, smallest_even_indices