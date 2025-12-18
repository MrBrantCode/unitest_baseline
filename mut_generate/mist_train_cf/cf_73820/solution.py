"""
QUESTION:
Implement a function `insertion_sort(arr)` that sorts a list of elements in ascending order. The function should be able to handle a list containing multiple data types (integers, floats, and strings), sorting integers and floats in numerical order and strings in alphabetical order. The function should not use any built-in sort functions and should have a time complexity of O(n^2).
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        next_element = arr[i]
        # Compare the current element with next one
        while (arr[j] > next_element) and (j >= 0):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = next_element
    return arr