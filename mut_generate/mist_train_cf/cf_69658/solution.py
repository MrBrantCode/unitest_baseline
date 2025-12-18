"""
QUESTION:
Write a function named `sort_descending` that takes a list as input and returns the list in descending order without using the `reverse()` or `sort()` methods.
"""

def sort_descending(lst):
    for i in range(len(lst)-1):
        for j in range(0, len(lst) - i - 1):
            if lst[j] < lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst