"""
QUESTION:
Given an integer n, find the closest integer (not including itself), which is a palindrome. 

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:

Input: "123"
Output: "121"



Note:

The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
"""

def find_nearest_palindrome(n: str) -> str:
    K = len(n)
    candidates = set([10 ** K + 1, 10 ** (K - 1) - 1])
    Prefix = int(n[:(K + 1) // 2])
    for start in map(str, [Prefix - 1, Prefix, Prefix + 1]):
        candidates.add(start + [start, start[:-1]][K & 1][::-1])
    candidates.discard(n)
    return str(min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x))))