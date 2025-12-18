"""
QUESTION:
Given two arrays `a` and `b`, each of size `n`, write a function called `sum_arrays` to compute the sum of all elements in the following manner: for each element `a[i]` in `a`, add `a[i]` and all elements in `b` from `b[0]` to `b[i-1]` to the sum. The function should return the final sum. The time complexity of the function should be optimized to O(n).
"""

def sum_arrays(a, b):
    total_sum = 0
    sum_b = sum(b)
    for i, num in enumerate(a):
        total_sum += num + sum(b[:i])
    return total_sum