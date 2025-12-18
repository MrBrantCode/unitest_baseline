"""
QUESTION:
Write a function `last_occurrence(arr, num)` that finds the last occurrence of `num` in the array `arr`. The array `arr` contains positive integers, has a maximum length of 10^6, and each element is between 1 and 10^6 (inclusive). If `num` does not exist in `arr`, return -1.
"""

def last_occurrence(arr, num):
    last_index = -1
    for i in range(len(arr)):
        if arr[i] == num:
            last_index = i
    return last_index