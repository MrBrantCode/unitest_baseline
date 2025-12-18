"""
QUESTION:
Write a function named `find_nth_largest` that takes a list of integers and an integer `n` as input, and returns the index of the `n`th largest element in the original list. The input list may contain duplicate elements.
"""

def find_nth_largest(lst, n):
    sorted_list = sorted(lst, reverse=True)
    nth_largest = sorted_list[n-1]
    index = lst.index(nth_largest)
    return index