"""
QUESTION:
Create a function called `reverseArray` that takes an array and two indices `start` and `end` as parameters. The function should reverse the elements of the array in-place, without using any additional data structures, and have a time complexity of O(n).
"""

def reverseArray(arr, start, end):
    if start >= end:
        return arr
    else:
        arr[start], arr[end] = arr[end], arr[start]
        return reverseArray(arr, start + 1, end - 1)