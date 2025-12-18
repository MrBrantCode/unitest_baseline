"""
QUESTION:
Write a function named `split_array` that takes a list of integers as input, splits it into two equally-sized subarrays in ascending order, and returns a tuple containing the two subarrays. The function should have a time complexity of O(nlogn) and a space complexity of O(1).
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