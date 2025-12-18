"""
QUESTION:
Implement a recursive function `countDivisible(arr, k, m)` that takes a two-dimensional array `arr`, an integer `k`, and an integer `m` as input, and returns the number of elements in `arr` that are divisible by `k` and have a remainder of 1 when divided by `m`. The array contains only positive integers.
"""

def countDivisible(arr, k, m):
    count = 0

    if len(arr) == 0:
        return count

    for element in arr[0]:
        if element % k == 0 and element % m == 1:
            count += 1

    return count + countDivisible(arr[1:], k, m)