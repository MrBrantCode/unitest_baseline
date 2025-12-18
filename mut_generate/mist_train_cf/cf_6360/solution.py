"""
QUESTION:
Design a function `remove_even_duplicates` that takes a list of integers as input, removes all even elements, and returns a new list containing the remaining odd elements without duplicates, preserving their original order is not required but the output list should not contain any duplicate elements. The input list can contain any number of elements.
"""

def remove_even_duplicates(lst):
    # Create an empty set to store unique odd elements
    odd_set = set()

    # Iterate through the list and add odd elements to the set
    for num in lst:
        if num % 2 != 0:
            odd_set.add(num)

    # Convert the set back to a list and return it
    return list(odd_set)