"""
QUESTION:
Write a function named `shuffle_array` that takes an array of integers as input and returns a new array where no two adjacent elements have a difference greater than 1 and the difference between the minimum and maximum values is minimized. The time complexity of the function should not exceed O(n log n), where n is the length of the array. The function should rearrange the elements from the original array and not use any additional elements.
"""

def shuffle_array(arr):
    arr.sort()

    left = 0
    right = len(arr) - 1

    result = []

    while left <= right:
        result.append(arr[left])
        left += 1

        if left <= right:
            result.append(arr[right])
            right -= 1

    return result