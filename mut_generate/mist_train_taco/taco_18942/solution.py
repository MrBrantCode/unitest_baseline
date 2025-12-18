"""
QUESTION:
Takahashi has N balls. Initially, an integer A_i is written on the i-th ball.

He would like to rewrite the integer on some balls so that there are at most K different integers written on the N balls.

Find the minimum number of balls that Takahashi needs to rewrite the integers on them.

Constraints

* 1 \leq K \leq N \leq 200000
* 1 \leq A_i \leq N
* All input values are integers.

Input

Input is given from Standard Input in the following format:


N K
A_1 A_2 ... A_N


Output

Print the minimum number of balls that Takahashi needs to rewrite the integers on them.

Examples

Input

5 2
1 1 2 2 5


Output

1


Input

4 4
1 1 2 2


Output

0


Input

10 3
5 1 3 2 4 1 1 2 3 4


Output

3
"""

from collections import Counter

def min_balls_to_rewrite(N, K, A):
    # Count the frequency of each integer on the balls
    ctr = Counter(A)
    
    # Get the counts of each integer and sort them
    cnts = sorted(ctr.values())
    
    # Calculate the minimum number of balls to rewrite
    ans = N - sum(cnts[-K:])
    
    return ans