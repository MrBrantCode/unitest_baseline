"""
QUESTION:
There are N stones, numbered 1, 2, \ldots, N. For each i (1 \leq i \leq N), the height of Stone i is h_i.

There is a frog who is initially on Stone 1. He will repeat the following action some number of times to reach Stone N:

* If the frog is currently on Stone i, jump to one of the following: Stone i + 1, i + 2, \ldots, i + K. Here, a cost of |h_i - h_j| is incurred, where j is the stone to land on.



Find the minimum possible total cost incurred before the frog reaches Stone N.

Constraints

* All values in input are integers.
* 2 \leq N \leq 10^5
* 1 \leq K \leq 100
* 1 \leq h_i \leq 10^4

Input

Input is given from Standard Input in the following format:


N K
h_1 h_2 \ldots h_N


Output

Print the minimum possible total cost incurred.

Examples

Input

5 3
10 30 40 50 20


Output

30


Input

3 1
10 20 10


Output

20


Input

2 100
10 10


Output

0


Input

10 4
40 10 20 70 80 10 20 70 80 60


Output

40
"""

def minimum_cost_to_reach_end(N: int, K: int, h: list) -> int:
    dp = [10 ** 10] * N
    dp[0] = 0
    
    for i in range(N - 1):
        for j in range(1, min(i + 1, K) + 1):
            dp[i + 1] = min(dp[i + 1], dp[i + 1 - j] + abs(h[i + 1] - h[i + 1 - j]))
    
    return dp[N - 1]