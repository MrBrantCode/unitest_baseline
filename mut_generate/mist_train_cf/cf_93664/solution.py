"""
QUESTION:
Implement a function called `bubble_sort` that sorts a list of strings in alphabetical order, ignoring case sensitivity, and considering ASCII values for non-alphabetical characters. The function should not use any built-in sorting functions or libraries. It should take a list of strings as input and return the sorted list.
"""

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j].lower() > lst[j+1].lower():
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst