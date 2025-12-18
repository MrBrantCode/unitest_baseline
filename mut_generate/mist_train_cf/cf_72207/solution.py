"""
QUESTION:
Write a function named sortEven that takes a list of integers as its argument. The function should return a new list where elements at odd indexes are in their original order, and elements at even indexes are sorted in ascending order.
"""

def sortEven(lst):
    evens = sorted(lst[::2])
    for i in range(0, len(lst), 2):
        lst[i] = evens.pop(0)
    return lst