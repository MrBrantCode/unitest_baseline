"""
QUESTION:
Find the smallest positive integer not present in an array that can contain both positive and negative numbers. The function should be named `find_smallest_missing_positive_integer` and take an array of integers as input. It should have a time complexity of O(n) and a space complexity of O(1). If no positive integer is missing, the function should return the smallest positive integer greater than the maximum element in the array.
"""

def find_smallest_missing_positive_integer(arr):
    if not arr:
        return 1

    min_positive = 1
    for num in arr:
        if num > 0 and num == min_positive:
            min_positive += 1
        elif num > 0 and num < min_positive:
            min_positive = num + 1

    return min_positive