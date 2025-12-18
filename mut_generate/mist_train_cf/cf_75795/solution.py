"""
QUESTION:
You are given an array `nums` consisting of unique positive integers. Compute the number of quadruplets `(a, b, c, d)` such that `a*b` equals `c*d`, where `a`, `b`, `c`, and `d` are distinct elements of `nums`. The length of `nums` is between 1 and 1000 (inclusive), and each element in `nums` is between 1 and 10^4 (inclusive).
"""

from collections import defaultdict

def quadruplets(nums):
    product_map = defaultdict(list)
    n = len(nums)
    res = 0

    for i in range(n):
        for j in range(i+1, n):
            product = nums[i] * nums[j]
            for x, y in product_map[product]:
                if x != i and x != j and y != i and y != j:
                    res += 1 

            product_map[product].append((i, j))

    return res