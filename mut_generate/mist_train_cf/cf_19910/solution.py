"""
QUESTION:
Write a function called `find_second_largest` that takes a list of distinct positive integers as input, with a length of at least 10 and at most 10,000 elements. The function should return the second largest element from the list.
"""

def find_second_largest(numbers):
    if len(numbers) < 10:
        return "List must have at least 10 elements"
    elif len(numbers) > 10000:
        return "List size cannot exceed 10,000 elements"
    else:
        sorted_numbers = sorted(set(numbers))
        return sorted_numbers[-2]