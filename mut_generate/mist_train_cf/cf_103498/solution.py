"""
QUESTION:
Write a function `count_occurrences(arr, target)` that counts the number of occurrences of a given integer `target` in an array `arr` containing up to 1 million integer elements. The function should have a time complexity of O(n) or better.
"""

def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count