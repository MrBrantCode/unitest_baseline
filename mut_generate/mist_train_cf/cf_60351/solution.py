"""
QUESTION:
Write a function `odd_triplets(n)` that calculates the total number of odd-triplets for a given `n`, where an odd-triplet is defined as `[n,k,f(n, k)]` with all three parameters being odd numbers. Here, `f(n, k)` represents the count of `k`-element subsets from the set of consecutive integers from 1 to `n` that yield an odd sum when their elements are added together. The function should be able to handle large values of `n`, such as `10^12`, and should return the total count of odd-triplets for `n` value up to the given number.
"""

from math import log2

def odd_triplets(n):
    limit = int(log2(n))
    cnt = 0
    for i in range(limit, -1, -1):
        j = n - (1<<i)
        if j < i:
            break
        cnt += 2**(min(i, j-i)-1) - 2**(i//2-1)
        cnt += 2**(min(i-1, j-i)-1) - 2**((i-1)//2-1)
    return cnt