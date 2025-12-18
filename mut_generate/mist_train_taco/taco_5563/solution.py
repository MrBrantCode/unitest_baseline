"""
QUESTION:
Input

The input contains two integers N, M (1 ≤ N ≤ 1024, 2 ≤ M ≤ 16), separated by a single space.

Output

Output "YES" or "NO".

Examples

Input


2 3


Output


YES


Input


3 2


Output


NO


Input


33 16


Output


YES


Input


26 5


Output


NO
"""

def can_be_represented_in_base(N: int, M: int) -> str:
    S = set()
    while N:
        remainder = N % M
        if remainder in S:
            return 'NO'
        else:
            S.add(remainder)
        N //= M
    return 'YES'