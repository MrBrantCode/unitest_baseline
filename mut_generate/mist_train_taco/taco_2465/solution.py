"""
QUESTION:
A sequence a0, a1, ..., at - 1 is called increasing if ai - 1 < ai for each i: 0 < i < t.

You are given a sequence b0, b1, ..., bn - 1 and a positive integer d. In each move you may choose one element of the given sequence and add d to it. What is the least number of moves required to make the given sequence increasing?

Input

The first line of the input contains two integer numbers n and d (2 ≤ n ≤ 2000, 1 ≤ d ≤ 106). The second line contains space separated sequence b0, b1, ..., bn - 1 (1 ≤ bi ≤ 106).

Output

Output the minimal number of moves needed to make the sequence increasing.

Examples

Input

4 2
1 3 3 2


Output

3
"""

import math

def min_moves_to_increasing_sequence(n, d, sequence):
    moves = 0
    for i in range(1, n):
        if sequence[i] > sequence[i - 1]:
            continue
        diff = sequence[i - 1] - sequence[i] + 1
        moves += math.ceil(diff / d)
        sequence[i] += d * math.ceil(diff / d)
    return moves