"""
QUESTION:
Write a function named `binary_gap` that takes an integer `n` as input and returns the maximum span between any two successive `1`s in the binary representation of `n`. If no such pair of `1's` exists, the function should return `0`. The function should be able to handle integers `n` where `1 <= n <= 10^9`.
"""

def binary_gap(n):
    binary = bin(n)[2:]
    max_gap = 0
    curr_gap = 0

    for b in binary:
        if b == '1':
            if curr_gap > max_gap:
                max_gap = curr_gap
            curr_gap = 0
        else:
            curr_gap += 1

    return max_gap