"""
QUESTION:
Write a function `countDivisible(arr, k, m)` that takes a two-dimensional array `arr` of positive integers, and two positive integers `k` and `m`, and returns the count of elements in `arr` that are divisible by `k` and have a remainder of 1 when divided by `m`. The function should use recursion to traverse the array.
"""

def countDivisible(arr, k, m):
    count = 0

    if len(arr) == 0:
        return count

    for element in arr[0]:
        if element % k == 0 and element % m == 1:
            count += 1

    return count + countDivisible(arr[1:], k, m)