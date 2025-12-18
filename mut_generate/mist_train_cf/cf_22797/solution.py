"""
QUESTION:
Given an array of positive integers and a target number, write a function last_occurrence(arr, num) that returns the last index of the target number in the array. The array can have a maximum length of 10^6 and each element can have a value between 1 and 10^6 (inclusive). If the target number does not exist in the array, return -1.
"""

def last_occurrence(arr, num):
    last_index = -1
    for i in range(len(arr)):
        if arr[i] == num:
            last_index = i
    return last_index