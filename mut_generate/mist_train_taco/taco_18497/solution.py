"""
QUESTION:
Problem

Given a natural number N less than or equal to 12, find the smallest natural number such that the number of divisors is exactly N.

Constraints

* 1 ≤ N ≤ 12

Input

One natural number N is given in one line.

Output

Output the smallest natural number on a line so that the number of divisors is exactly N.

Examples

Input

1


Output

1


Input

2


Output

2


Input

3


Output

4
"""

def find_smallest_number_with_n_divisors(n):
    for i in range(1, 10000):
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
        if cnt == n:
            return i