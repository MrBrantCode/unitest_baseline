"""
QUESTION:
Implement the function `peculiar_ordering` that accepts a list of integers and/or decimal numbers and/or None values. The function should return the list sorted in a peculiar manner that starts with the smallest value, then takes the maximum of the remaining numbers followed by the minimum of the rest and so on, while ignoring None values.
"""

def peculiar_ordering(lst):
    # Filter out None values
    lst = [val for val in lst if val is not None]
    # Sort the list in descending order
    lst.sort(reverse=True)

    result = []
    while lst:
        # Take the smallest element (which is at the end of the list)
        result.append(lst.pop())
        if lst:
            # Take the largest element (which is at the beginning of the list)
            result.append(lst.pop(0))
    
    return result