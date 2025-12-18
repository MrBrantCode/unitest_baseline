"""
QUESTION:
Create a function called `find_5th_smallest_number` that takes an array of floats as input and returns the 5th smallest number in the array without using built-in sorting methods. The function should instead implement a custom sorting algorithm using conditional statements and loops.
"""

def find_5th_smallest_number(arr):
    def find_min_from_index(arr, index):
        min_index = index
        n = len(arr)
        for i in range(index + 1, n):
            if arr[i] < arr[min_index]:
                min_index = i
        return min_index

    n = len(arr)
    for i in range(n):
        min_index = find_min_from_index(arr, i)
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr[4]