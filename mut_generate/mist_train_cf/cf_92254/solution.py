"""
QUESTION:
Write a function named `reverse_combine_sort` that takes two lists as input, reverses the elements of each list, combines the reversed lists into a single list, and returns the combined list sorted in ascending order. The function should be able to handle lists containing any type of elements that can be compared with each other.
"""

def reverse_combine_sort(list1, list2):
    return sorted(list1[::-1] + list2[::-1])