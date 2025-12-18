"""
QUESTION:
Write a function `max_product_indices` that takes a list of integers as input and returns a pair of unique indices whose corresponding elements have the maximum product. The function should handle edge cases including empty lists, lists with one element, and lists with negative integers and zeros.
"""

def max_product_indices(lst):
    # Handle edge case: empty list
    if len(lst) == 0:
        return []

    # Handle edge case: list has only one element
    if len(lst) == 1:
        return [0]

    # Handle case: list has two or more elements  
    # Sort the list along with the indices
    lst_with_indices = sorted((value, i) for i, value in enumerate(lst))
    
    # Calculate the product of the two lowest numbers (possibly negative)
    lowest_product = lst_with_indices[0][0] * lst_with_indices[1][0]
    
    # Calculate the product of the two highest numbers
    highest_product = lst_with_indices[-1][0] * lst_with_indices[-2][0]
    
    # Return either the indices of the lowest two or highest two numbers, whichever product is larger
    if lowest_product > highest_product:
        return sorted([lst_with_indices[0][1], lst_with_indices[1][1]])
    else:
        return sorted([lst_with_indices[-1][1], lst_with_indices[-2][1]])