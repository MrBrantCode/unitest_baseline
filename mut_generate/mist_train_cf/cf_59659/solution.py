"""
QUESTION:
Write a function named `subarrayBitwiseORs` that takes a list of non-negative integers as input and returns a tuple of three integers. The function should calculate the number of unique possible results from the bitwise OR operation on all possible subarrays, the maximum possible result, and the minimum possible result.

The input list `arr` has a length between 1 and 50,000 (inclusive), and each element in the list is a non-negative integer between 0 and 1,000,000,000 (inclusive). The function should return a tuple where the first element is the count of unique possible results, the second element is the maximum possible result, and the third element is the minimum possible result.
"""

def subarrayBitwiseORs(arr):
    res = set()
    cur = set()
    for i in arr:
        cur = {i | j for j in cur} | {i}
        res |= cur
    return len(res), max(res), min(res)