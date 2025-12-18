"""
QUESTION:
Create a function that returns an array containing the first `l` digits from the `n`th diagonal of [Pascal's triangle](https://en.wikipedia.org/wiki/Pascal's_triangle).

`n = 0` should generate the first diagonal of the triangle (the 'ones'). The first number in each diagonal should be 1.

If `l = 0`, return an empty array. Assume that both `n` and `l` will be non-negative integers in all test cases.
"""

def generate_pascals_diagonal(n, l):
    if l == 0:
        return []
    
    result = [1]
    for k in range(1, l):
        result.append(result[-1] * (n + k) // k)
    
    return result