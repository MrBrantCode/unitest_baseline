"""
QUESTION:
You are asked to write a function named `quantum_entanglement`. The function should accept two parameters: a string `n` and an integer `k`. The string `n` is a sequence of characters, each of which is either '0' or '1'. The integer `k` represents the number of entanglements. The function should return a string where all substrings of length `k` are entangled.
"""

def quantum_entanglement(n, k):
    n = list(n)
    for i in range(0, len(n), k):
        ones = n[i:i+k].count('1')
        n[i:i+k] = ['1'] * ones + ['0'] * (k - ones)
    return ''.join(n)