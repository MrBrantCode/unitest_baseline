"""
QUESTION:
Write a function `find_second_largest_index(arr)` that finds the index of the second largest element in the given array `arr`. The function should have a time complexity of O(n), where n is the size of the array, and should not use any built-in sorting or max/min functions. If no second largest element exists, return the result as -1 or any other appropriate value to indicate the absence of a second largest element.
"""

def find_second_largest_index(arr):
    n = len(arr)
    max_index = -1
    second_max_index = -1

    for i in range(n):
        if max_index == -1 or arr[i] > arr[max_index]:
            second_max_index = max_index
            max_index = i
        elif second_max_index == -1 or arr[i] > arr[second_max_index] and arr[i] != arr[max_index]:
            second_max_index = i

    return second_max_index