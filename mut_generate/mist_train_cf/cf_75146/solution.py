"""
QUESTION:
Write a function named `solve` that takes a list of integers `l` and an integer `m` as input. The function should return the product of `m` and the sum of all numbers in `l` that are less than `m` after being multiplied by 2. If no numbers in `l` are less than `m`, the function should return -1. The function must have a time complexity of better than O(n^2), where n is the number of elements in `l`.
"""

def solve(l, m):
    sum = 0
    for i in l:
        if i < m:
            sum += i * 2
    if sum > 0:
        return sum * m
    return -1