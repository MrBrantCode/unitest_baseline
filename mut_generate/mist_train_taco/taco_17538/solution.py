"""
QUESTION:
You are given a permutation p = (p_1, \ldots, p_N) of \\{ 1, \ldots, N \\}. You can perform the following two kinds of operations repeatedly in any order:

* Pay a cost A. Choose integers l and r (1 \leq l < r \leq N), and shift (p_l, \ldots, p_r) to the left by one. That is, replace p_l, p_{l + 1}, \ldots, p_{r - 1}, p_r with p_{l + 1}, p_{l + 2}, \ldots, p_r, p_l, respectively.
* Pay a cost B. Choose integers l and r (1 \leq l < r \leq N), and shift (p_l, \ldots, p_r) to the right by one. That is, replace p_l, p_{l + 1}, \ldots, p_{r - 1}, p_r with p_r, p_l, \ldots, p_{r - 2}, p_{r - 1}, respectively.



Find the minimum total cost required to sort p in ascending order.

Constraints

* All values in input are integers.
* 1 \leq N \leq 5000
* 1 \leq A, B \leq 10^9
* (p_1 \ldots, p_N) is a permutation of \\{ 1, \ldots, N \\}.

Input

Input is given from Standard Input in the following format:


N A B
p_1 \cdots p_N


Output

Print the minimum total cost required to sort p in ascending order.

Examples

Input

3 20 30
3 1 2


Output

20


Input

4 20 30
4 2 3 1


Output

50


Input

1 10 10
1


Output

0


Input

4 1000000000 1000000000
4 3 2 1


Output

3000000000


Input

9 40 50
5 3 4 7 6 1 2 9 8


Output

220
"""

def minimum_sort_cost(N, A, B, p):
    Q = [0] * N
    for (i, p_val) in enumerate(p):
        Q[p_val - 1] = i
    
    INF = 10 ** 18
    dp = [[INF] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    
    for i in range(N):
        qi = Q[i]
        for j in range(N):
            v = dp[i][j]
            dp[i + 1][j] = min(dp[i + 1][j], v + (A if qi < j else B))
            dp[i][j + 1] = min(dp[i][j + 1], v)
            if Q[i] == j:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], v)
    
    for i in range(N):
        dp[i + 1][N] = min(dp[i + 1][N], dp[i][N] + A)
    
    for j in range(N):
        dp[N][j + 1] = min(dp[N][j + 1], dp[N][j])
    
    return dp[N][N]