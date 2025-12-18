"""
QUESTION:
There are N Reversi pieces arranged in a row. (A Reversi piece is a disc with a black side and a white side.) The state of each piece is represented by a string S of length N. If S_i=`B`, the i-th piece from the left is showing black; If S_i=`W`, the i-th piece from the left is showing white.

Consider performing the following operation:

* Choose i (1 \leq i < N) such that the i-th piece from the left is showing black and the (i+1)-th piece from the left is showing white, then flip both of those pieces. That is, the i-th piece from the left is now showing white and the (i+1)-th piece from the left is now showing black.



Find the maximum possible number of times this operation can be performed.

Constraints

* 1 \leq |S| \leq 2\times 10^5
* S_i=`B` or `W`

Input

Input is given from Standard Input in the following format:


S


Output

Print the maximum possible number of times the operation can be performed.

Examples

Input

BBW


Output

2


Input

BWBWBW


Output

6
"""

def max_reversi_operations(S: str) -> int:
    num = 0
    st = 0
    for i, x in enumerate(S):
        if x == 'W':
            num += i - st
            st += 1
    return num