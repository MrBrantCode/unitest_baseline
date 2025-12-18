"""
QUESTION:
The function `peculiar_ordering` should take in a list of integers, decimal numbers, and None values. It should return a sorted list following these rules: 
- Start with the smallest value.
- Next, pick out the maximum among the remaining numbers.
- Then find the minimum out of the remaining numbers and so on.
- Ignore None values.

The function should be efficient and correctly implement the unusual sorting order.
"""

def peculiar_ordering(lst):
    lst = [val for val in lst if val is not None] # Remove None values
    sorted_list = sorted(lst, reverse=True) # Sort list in reverse order

    result = []
    while sorted_list:
        if sorted_list:
            result.append(sorted_list.pop())  # pick up smallest
        if sorted_list:
            result.append(sorted_list.pop(0))  # pick up largest

    return result