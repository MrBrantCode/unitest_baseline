"""
QUESTION:
Write a function named `knapSack(W, wt, val, n)` that returns the maximum value that can be put in a knapsack of capacity `W` using `n` items, each with a weight `wt` and their respective values `val`. The function should use dynamic programming with tabulation and memoization to account for interdependencies, overlapping sub-problems, and constrained resources. The weights and values are given as lists of integers, and the capacity is an integer.
"""

def knapSack(W, wt, val, n):
    # Table to store results of subproblems
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]],  K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][W]