"""
QUESTION:
Input

The input contains two integers a1, a2 (0 ≤ ai ≤ 109), separated by a single space.

Output

Output a single integer.

Examples

Input

3 14


Output

44


Input

27 12


Output

48


Input

100 200


Output

102
"""

from math import floor

def calculate_sum_with_reversed_second_number(a1: int, a2: int) -> int:
    rev = 0
    while a2 > 0:
        a = int(a2 % 10)
        rev = rev * 10 + a
        a2 = floor(a2 / 10)
    return a1 + rev