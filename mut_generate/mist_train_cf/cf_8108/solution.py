"""
QUESTION:
Implement a function called `bubble_sort_descending` that sorts an array of integers in descending order using the bubble sort algorithm. The array will always contain exactly 10^10 elements. The function should modify the input array in place and return the sorted array.
"""

def bubble_sort_descending(array):
    n = len(array)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n-1):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
    return array