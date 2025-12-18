"""
QUESTION:
Given two integers `n` and `start`, generate a permutation `p` of the sequence `(0,1,2.....,2^n -1)` where the first element of the permutation `p[0]` equals `start`, each pair of consecutive elements `p[i]` and `p[i+1]` differ by a single bit in their binary representation, and the first and last elements of the permutation `p[0]` and `p[2^n -1]` also differ by just one bit in their binary representation. The constraints are: `1 <= n <= 16` and `0 <= start < 2 ^ n`.
"""

def circular_permutation(n: int, start: int):
    gray = [0]
    for i in range(n):
        gray = gray + [x + (1 << i) for x in reversed(gray)]
    return gray[gray.index(start):] + gray[:gray.index(start)]