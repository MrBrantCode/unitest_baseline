"""
QUESTION:
Create a function named `evenify` that takes two lists of integers as parameters, `seq1` and `seq2`. The function should determine if it is possible to swap elements between `seq1` and `seq2` such that all elements in `seq1` become even, while maintaining the overall sum of both sequences. The function should return "YES" if such a transformation is possible and "NO" otherwise. The function assumes that both input sequences will have at least one integer.
"""

def evenify(seq1, seq2):
    has_even = any(n % 2 == 0 for n in seq1 + seq2)
    has_odd = any(n % 2 == 1 for n in seq1 + seq2)
    return "YES" if has_even and has_odd else "NO"