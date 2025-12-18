"""
QUESTION:
Write a function named `sort_third` that takes a list of integers as input, sorts every third element in ascending order, and returns the modified list. The function should replace every third element in the original list with the sorted elements, keeping the other elements in their original positions.
"""

def sort_third(l):
    aux = [l[i] for i in range(0, len(l), 3)]
    aux.sort()
    for i in range(0, len(l), 3):
        l[i] = aux.pop(0)
    return l