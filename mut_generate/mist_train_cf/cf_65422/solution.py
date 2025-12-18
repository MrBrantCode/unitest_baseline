"""
QUESTION:
Create a function called `insertion_sort` that takes a list of numbers as input and returns the sorted list using the insertion sort algorithm. The function should sort the list in ascending order.
"""

def insertion_sort(lst):
    for i in range(1, len(lst)):
        current_element = lst[i]
        pos = i
        while current_element < lst[pos - 1] and pos > 0:
            lst[pos] = lst[pos - 1]
            pos = pos - 1
        lst[pos] = current_element
    return lst