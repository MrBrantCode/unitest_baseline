"""
QUESTION:
Jack is working on his jumping skills recently. Currently he's located at point zero of the number line. He would like to get to the point x. In order to train, he has decided that he'll first jump by only one unit, and each subsequent jump will be exactly one longer than the previous one. He can go either left or right with each jump. He wonders how many jumps he needs to reach x.

Input

The input data consists of only one integer x ( - 109 ≤ x ≤ 109).

Output

Output the minimal number of jumps that Jack requires to reach x.

Examples

Input

2


Output

3


Input

6


Output

3


Input

0


Output

0
"""

from math import sqrt

def minimal_jumps_to_reach(x: int) -> int:
    x = abs(x)
    n = int((sqrt(1 + 8 * x) - 1) / 2)
    k = n * (n + 1) // 2
    
    if k == x:
        return n
    else:
        n += 1
        k += n
        if (k - x) % 2:
            n += 1
            k += n
            return n + (k - x) % 2
        else:
            return n