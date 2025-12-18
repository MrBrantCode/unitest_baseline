"""
QUESTION:
Create a function called `add_lists` that takes two lists of numbers, `list1` and `list2`, as input and returns a new list containing the element-wise sums of the two input lists. The function should be able to handle lists of varying lengths, treating missing elements in the shorter list as zero.
"""

from itertools import zip_longest

def add_lists(list1, list2):
    result = []
    for num1, num2 in zip_longest(list1, list2, fillvalue=0):
        result.append(num1 + num2)
    return result