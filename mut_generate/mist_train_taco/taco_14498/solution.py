"""
QUESTION:
Give a pair of integers (A, B) such that A^5-B^5 = X. It is guaranteed that there exists such a pair for the given integer X.

Constraints

* 1 \leq X \leq 10^9
* X is an integer.
* There exists a pair of integers (A, B) satisfying the condition in Problem Statement.

Input

Input is given from Standard Input in the following format:


X


Output

Print A and B, with space in between. If there are multiple pairs of integers (A, B) satisfying the condition, you may print any of them.


A B

Output

Print A and B, with space in between. If there are multiple pairs of integers (A, B) satisfying the condition, you may print any of them.


A B

Examples

Input

33


Output

2 -1


Input

1


Output

0 -1
"""

def find_a_b_for_x(X: int) -> tuple:
    for a in range(999):
        for b in range(-a, a):
            if a ** 5 - b ** 5 == X:
                return (a, b)
    return None  # This line should never be reached due to the problem's guarantee