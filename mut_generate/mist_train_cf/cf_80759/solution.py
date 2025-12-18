"""
QUESTION:
You are given an integer `n` representing the length of an array where the i-th element is `(2 * i) + 1`, and an integer `m` representing the maximum number of times an index can be selected. Your task is to return the least number of operations required to equalize all the elements of the array, where in one operation you can decrement 1 from `arr[x]` and increment 1 to `arr[y]`, subject to the restriction that each index can be selected at most `m` times. If it is unfeasible to equalize all elements with this limitation, return -1.

Restrictions: `1 <= n <= 10^4` and `1 <= m <= n`.
"""

def entrance(n, m):
    result = (n - m) * n - (n - m) * (n - m + 1) 
    return result if result >= 0 else -1