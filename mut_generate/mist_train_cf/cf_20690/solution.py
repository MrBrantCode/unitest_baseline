"""
QUESTION:
Given two arrays of integers, implement a function `find_swap_values(arr1, arr2)` to find a pair of values (one from each array) that can be swapped to make the sums of the two arrays equal. The function should not use any additional data structures or libraries and should have a time complexity of O(n log n) or better. If no such pair is found or if it's impossible to find a pair (i.e., the difference between the sums is odd), the function should return an empty array.
"""

def find_swap_values(arr1, arr2):
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    diff = sum1 - sum2

    if diff % 2 != 0:
        return []

    arr1.sort()
    arr2.sort()

    pointer1 = 0
    pointer2 = 0

    while pointer1 < len(arr1) and pointer2 < len(arr2):
        current_diff = arr1[pointer1] - arr2[pointer2]

        if current_diff == diff / 2:
            return [arr1[pointer1], arr2[pointer2]]
        elif current_diff < diff / 2:
            pointer1 += 1
        else:
            pointer2 += 1

    return []