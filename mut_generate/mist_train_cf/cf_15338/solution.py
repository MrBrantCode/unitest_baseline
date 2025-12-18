"""
QUESTION:
Implement a function named bubble_sort that takes a list of strings as input and returns the sorted list in alphabetical order, ignoring case sensitivity and using ASCII values for comparison. The function should not use any built-in sorting functions or libraries, instead using a manual sorting algorithm.
"""

def entrance(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j].lower() > lst[j+1].lower():
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst