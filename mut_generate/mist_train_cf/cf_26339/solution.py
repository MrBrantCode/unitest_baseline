"""
QUESTION:
Write a function `two_sum_elements` that takes an array of integers and a target integer as input, and returns an array containing two elements from the input array that sum up to the target. The function should return `None` if no such pair exists.
"""

def two_sum_elements(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [arr[i], arr[j]]
    return None