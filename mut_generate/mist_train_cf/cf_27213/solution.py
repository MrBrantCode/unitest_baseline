"""
QUESTION:
Implement a function named `custom_sort` that takes a list of integers as input and returns the sorted list in ascending order using a custom sorting algorithm. The custom sorting algorithm should be a variation of the quicksort algorithm, where the partitioning step chooses the median of the first, middle, and last elements of the list as the pivot. If the input list has one or zero elements, the function should return the original list.
"""

def custom_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = median_of_three(arr[0], arr[len(arr)//2], arr[-1])
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return custom_sort(less) + equal + custom_sort(greater)

def median_of_three(a, b, c):
    if a < b < c or c < b < a:
        return b
    elif b < a < c or c < a < b:
        return a
    else:
        return c