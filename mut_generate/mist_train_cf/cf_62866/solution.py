"""
QUESTION:
Create a function named `bubble_sort` that takes a list of integers as input and returns the list sorted in ascending order using the Bubble Sort algorithm. The input list can be any length, and the function should modify the original list in-place, returning the sorted list.
"""

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n - i - 1): 
            # Swap if current element is greater than the next
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return array