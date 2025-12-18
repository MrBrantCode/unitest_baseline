"""
QUESTION:
You are given positive integers X and Y. If there exists a positive integer not greater than 10^{18} that is a multiple of X but not a multiple of Y, choose one such integer and print it. If it does not exist, print -1.

Constraints

* 1 ≤ X,Y ≤ 10^9
* X and Y are integers.

Input

Input is given from Standard Input in the following format:


X Y


Output

Print a positive integer not greater than 10^{18} that is a multiple of X but not a multiple of Y, or print -1 if it does not exist.

Examples

Input

8 6


Output

16


Input

3 3


Output

-1
"""

def find_multiple_not_divisible_by(X: int, Y: int) -> int:
    if X % Y == 0:
        return -1
    else:
        return X