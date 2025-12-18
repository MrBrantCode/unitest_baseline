"""
QUESTION:
Find the `find_nth_lexico_permutation` of a given number `n` in lexicographic order. The function takes two parameters: `n` (the position of the permutation) and `elements` (the number of distinct entities). Return the permutation as a string. The function should use 0-based indexing for the position, i.e., the first permutation is at position 0.
"""

from math import factorial

def find_nth_lexico_permutation(n, elements):
    numbers = list(range(elements))
    permutation = []
    while numbers:
        f = factorial(len(numbers) - 1)
        i = n // f
        n %= f
        permutation.append(numbers.pop(i if n > 0 else i - 1))
    return ''.join(str(i) for i in permutation)