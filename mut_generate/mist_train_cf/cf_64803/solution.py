"""
QUESTION:
Write a function `reverse_bits(n)` that takes an integer `n` and reverses its binary representation using only bitwise operations. Then, write a function `reverse_array(arr)` that applies `reverse_bits(n)` to each element of the input array `arr`. Implement this for an array of integers.
"""

def reverse_bits(n):
    result = 0
    while n > 0:
        result = (result << 1) + (n & 1)
        n >>= 1
    return result

def entance(arr):
    return [reverse_bits(x) for x in arr]