"""
QUESTION:
Write a function `count_occurrences` that takes an array `arr` and a value `x` as arguments. The function should return the number of times `x` appears in `arr` with a time complexity of O(n) and without using any built-in methods or libraries. The array can contain up to 10^6 elements and `x` can be any integer between -10^9 and 10^9.
"""

def count_occurrences(arr, x):
    count = 0
    for num in arr:
        if num == x:
            count += 1
    return count