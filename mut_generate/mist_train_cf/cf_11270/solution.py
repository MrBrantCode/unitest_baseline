"""
QUESTION:
Write a function `find_smallest_positive(my_list)` that takes a list of integers as input and returns the smallest positive number that is not present in the list. The list may contain both positive and negative numbers, and the function should return a positive integer.
"""

def find_smallest_positive(my_list):
    num_set = set(my_list)
    i = 1
    while True:
        if i not in num_set:
            return i
        i += 1