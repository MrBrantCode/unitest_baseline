"""
QUESTION:
Develop a function named `smallest_distinct_integers` that takes a list of integers as input and returns the five smallest distinct integers within the list. The function should ignore repeated integers. The input list can contain any number of integers, but the function should only return the five smallest distinct integers. If the input list has less than five distinct integers, the function should return all distinct integers in the list.
"""

def smallest_distinct_integers(numbers):
    # Convert to set to remove duplicates, then back to list
    distinct_numbers = list(set(numbers))
    
    # Sort the list
    distinct_numbers.sort()
    
    # return the smallest 5 integers
    return distinct_numbers[:5]