"""
QUESTION:
Write a function `sort_list` that takes a list of strings representing numbers (which can be positive, negative, decimal, or in scientific notation) and returns the list sorted in ascending order. Implement a custom sorting algorithm without using the built-in sort function in Python.
"""

def sort_list(l):
    n = len(l)

    for i in range(n):
        for j in range(0, n-i-1):
            if float(l[j]) > float(l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]

    return l