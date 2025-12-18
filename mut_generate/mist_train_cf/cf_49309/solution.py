"""
QUESTION:
Write a function `nextGreaterElement(n)` that takes an integer `n` as input and returns a tuple of two integers. The first integer should be the smallest integer that has exactly the same digits existing in `n` and is greater in value than `n`. If no such positive integer exists, return `-1` for the first integer. The second integer should be the number of permutations of `n` that are greater than `n`. If there are no permutations greater than `n`, return `0`. The returned integers should fit in 32-bit integers. If there is a valid answer but it does not fit in 32-bit integer, return `-1` for the first integer. The input `n` is a positive integer and `1 <= n <= 2^31 - 1`.
"""

from math import factorial

def nextGreaterElement(n):
    digits = [int(d) for d in str(n)]
    
    # Find non-increasing suffix
    i = len(digits) - 1
    while i > 0 and digits[i - 1] >= digits[i]:
        i -= 1
    
    if i <= 0:
        return -1, 0
    
    # Find successor to pivot
    j = len(digits) - 1
    while digits[j] <= digits[i - 1]:
        j -= 1
    digits[i - 1], digits[j] = digits[j], digits[i - 1]
    
    # Reverse suffix
    digits[i : ] = digits[len(digits) - 1 : i - 1 : -1]
    
    # Check if result is within 32-bit integer limit
    next_greater = int(''.join(map(str, digits)))
    if next_greater > (2**31 - 1):
        return -1, 0
    
    # Calculate permutation count
    permutation_cnt = 1
    visited = set()
    for d in digits:
        permutation_cnt *= factorial(len(digits) - len(visited))
        permutation_cnt //= factorial(len(digits) - len(visited) - 1)
        visited.add(d)
    
    return next_greater, permutation_cnt - 1