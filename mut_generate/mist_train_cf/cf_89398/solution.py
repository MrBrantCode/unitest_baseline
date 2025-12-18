"""
QUESTION:
Write a function `remove_even_duplicates` that takes a list of integers as input, removes all even numbers, and returns a list of unique odd numbers in their original order. The input list should contain at least 50 elements. The function should preserve the original order of the elements and remove any duplicates.
"""

def remove_even_duplicates(lst):
    # Create an empty set to store unique odd elements
    odd_set = set()

    # Iterate through the list and add odd elements to the set
    for num in lst:
        if num % 2 != 0:
            odd_set.add(num)

    # Convert the set back to a list and return it
    return [num for num in lst if num in odd_set]