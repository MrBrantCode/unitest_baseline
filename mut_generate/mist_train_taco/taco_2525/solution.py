"""
QUESTION:
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:


Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:


Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

import math

def find_least_squares(n: int) -> int:
    while n % 4 == 0:
        n = n // 4
    if n % 8 == 7:
        return 4
    a = 0
    while a * a <= n:
        b = int(math.sqrt(n - a * a))
        if a * a + b * b == n:
            return (1 if a > 0 else 0) + (1 if b > 0 else 0)
        a += 1
    return 3