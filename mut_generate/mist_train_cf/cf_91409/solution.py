"""
QUESTION:
Implement the function `bubble_sort(lst)` to sort a given list of numbers in ascending order without using any built-in sorting functions or libraries. The function should take a list of numbers as input and return the sorted list.
"""

def entrance(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst