"""
QUESTION:
Find the function `find_second_largest(arr)` that takes an array of integers `arr` and returns a tuple containing the second largest number and its frequency in the array. If there are multiple numbers with the same frequency, return the smallest number among them. The function should have a time complexity of O(n) and not use any built-in sorting functions or data structures.
"""

def find_second_largest(arr):
    largest = float('-inf')
    second_largest = float('-inf')
    largest_freq = 0
    second_largest_freq = 0

    for num in arr:
        if num > largest:
            second_largest = largest
            second_largest_freq = largest_freq
            largest = num
            largest_freq = 1
        elif num == largest:
            largest_freq += 1
        elif num > second_largest:
            second_largest = num
            second_largest_freq = 1
        elif num == second_largest:
            second_largest_freq += 1

    return second_largest, second_largest_freq