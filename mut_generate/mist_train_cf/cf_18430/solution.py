"""
QUESTION:
Write a function `split_array` that takes a list of integers as input and returns a tuple of two lists. The function should split the input list into two equally-sized sublists, each sorted in ascending order. The function should have a time complexity of O(nlogn) and a space complexity of O(n).
"""

def split_array(arr):
    # Sort the input array
    arr.sort()

    # Find the middle index
    middle_index = len(arr) // 2

    # Split the array into two halves
    subarray1 = arr[:middle_index]
    subarray2 = arr[middle_index:]

    return subarray1, subarray2