"""
QUESTION:
Create a function named `insertion_sort_descending` that performs insertion sorting on a given list of integers in descending order. The function should take a list of integers as input and return the sorted list in descending order.
"""

def insertion_sort_descending(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key > lst[j] :
                lst[j + 1] = lst[j]
                j -= 1
        lst[j + 1] = key
    return lst