"""
QUESTION:
Implement a function named `insertion_sort` that takes a list of numbers as input and returns a new sorted list in ascending order. The function should use the insertion sort algorithm and modify the original list in-place. The input list can contain duplicate numbers.
"""

def insertionsort(lst):
    for i in range(len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst