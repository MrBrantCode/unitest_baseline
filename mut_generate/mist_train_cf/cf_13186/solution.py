"""
QUESTION:
Write a function `count_occurrences` that takes an array `arr` and an integer `x` as arguments. The function should return the number of occurrences of `x` in `arr`. The function should only iterate through `arr` once and must not use any built-in methods or libraries, with a time complexity of O(n).
"""

def count_occurrences(arr, x):
    count = 0
    for num in arr:
        if num == x:
            count += 1
    return count