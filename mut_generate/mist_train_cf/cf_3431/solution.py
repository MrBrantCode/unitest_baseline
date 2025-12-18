"""
QUESTION:
Write a recursive function `countTrailingZeroes` that calculates the number of trailing zeroes in a factorial number `n!`, where `n` is a non-negative integer. The function should have a time complexity of O(log n), use a constant amount of memory, and only use basic arithmetic operations. It should not use any additional data structures or arrays, loops, or iterative constructs.
"""

def countTrailingZeroes(n, count=0):
    if n < 5:
        return count
    numZeroes = n // 5
    return countTrailingZeroes(numZeroes, count + numZeroes)