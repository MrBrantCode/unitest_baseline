"""
QUESTION:
Implement a function `count_11_in_binary` that takes an integer `n` as input, and returns the total number of times the substring "11" appears in the binary representations of all integers from 1 to `n`.
"""

def count_11_in_binary(n):
    count = 0
    for i in range(1, n+1):
        binary_repr = bin(i)[2:]  # Remove '0b' prefix
        count += binary_repr.count('11')
    return count