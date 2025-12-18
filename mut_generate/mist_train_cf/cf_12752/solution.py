"""
QUESTION:
Write a function named `count_target` that takes an array of integers and a target integer as input, and returns the count of the target integer in the array.

The array can contain both positive and negative integers, with a length not exceeding 10^6, and the target integer can be any integer within the range of a 32-bit signed integer. The function should have a time complexity of O(n), where n is the length of the array.
"""

def count_target(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count