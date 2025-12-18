"""
QUESTION:
Create a function named `sum_of_list` that takes a list of integers as input and returns the sum of all the elements in the list. The function must not use any built-in sum() or reduce() functions, must have a time complexity of O(n), where n is the length of the input list, and must not use any explicit loops.
"""

def sum_of_list(lst, index=0):
    if index == len(lst):
        return 0
    else:
        return lst[index] + sum_of_list(lst, index + 1)