"""
QUESTION:
Write a function `remove_duplicates` that takes a list of integers as input, removes all duplicates from the list, sorts the list in ascending order, and returns the count of unique numbers in the list. The function should handle both positive and negative integers, as well as zero.
"""

def remove_duplicates(lst):
    unique_numbers = []
    for num in lst:
        if num not in unique_numbers:
            unique_numbers.append(num)
    unique_numbers.sort()
    return len(unique_numbers)