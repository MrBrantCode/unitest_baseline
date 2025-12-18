"""
QUESTION:
Create a function `get_max_triples(n)` that takes a positive integer `n` as input. Generate an array `a` of length `n` where `a[i] = (i * i - i + 1) + (i % 3)` for each `i` from 1 to `n`. Calculate the expression `(a[i] * a[j]) % a[k]` for all possible triples `(a[i], a[j], a[k])` where `i < j < k`. Return the number of triples where the result of the expression is a multiple of `n`.
"""

def get_max_triples(n):
    a = [(i * i - i + 1) + (i % 3) for i in range(1, n + 1)]
    return sum(
        1 
        for i in range(n) 
        for j in range(i + 1, n) 
        for k in range(j + 1, n) 
        if (a[i] * a[j]) % n == 0 and a[k] != 0 and (a[i] * a[j]) % a[k] == 0
    )