"""
QUESTION:
Everything is great about Ilya's city, except the roads. The thing is, the only ZooVille road is represented as n holes in a row. We will consider the holes numbered from 1 to n, from left to right.

Ilya is really keep on helping his city. So, he wants to fix at least k holes (perharps he can fix more) on a single ZooVille road. 

The city has m building companies, the i-th company needs ci money units to fix a road segment containing holes with numbers of at least li and at most ri. The companies in ZooVille are very greedy, so, if they fix a segment containing some already fixed holes, they do not decrease the price for fixing the segment. 

Determine the minimum money Ilya will need to fix at least k holes.

Input

The first line contains three integers n, m, k (1 ≤ n ≤ 300, 1 ≤ m ≤ 105, 1 ≤ k ≤ n). The next m lines contain the companies' description. The i-th line contains three integers li, ri, ci (1 ≤ li ≤ ri ≤ n, 1 ≤ ci ≤ 109).

Output

Print a single integer — the minimum money Ilya needs to fix at least k holes. 

If it is impossible to fix at least k holes, print -1.

Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is preferred to use the cin, cout streams or the %I64d specifier.

Examples

Input

10 4 6
7 9 11
6 9 13
7 7 7
3 5 6


Output

17


Input

10 7 1
3 4 15
8 9 8
5 6 8
9 10 6
1 4 2
1 4 10
8 10 13


Output

2


Input

10 1 9
5 10 14


Output

-1
"""

def minimum_cost_to_fix_holes(n, m, k, companies):
    # Initialize cost matrix with infinity
    cost = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
    
    # Fill the cost matrix with the minimum cost for each segment
    for (L, R, C) in companies:
        cost[L - 1][R] = min(cost[L - 1][R], C)
    
    # Update the cost matrix to ensure that cost[L][R] is the minimum cost for any segment ending at R starting from L
    for L in range(n + 1):
        for R in range(1, n + 1):
            cost[R][L] = min(cost[R][L], cost[R - 1][L])
    
    # Initialize the dp array with a large number (10^18)
    dp = [[10 ** 18 for _ in range(n + 1)] for _ in range(n + 1)]
    
    # Base case: No cost to fix 0 holes
    for i in range(n):
        dp[i][0] = 0
    
    # Fill the dp array
    for i in range(n):
        for j in range(i + 1):
            if dp[i][j] < 10 ** 18:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
                for k in range(i + 1, n + 1):
                    dp[k][j + k - i] = min(dp[k][j + k - i], dp[i][j] + cost[i][k])
    
    # The answer is the minimum cost to fix at least k holes
    ans = dp[n][k]
    return ans if ans < 10 ** 18 else -1