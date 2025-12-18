"""
QUESTION:
Write a Python function named `knapSack` that solves the 0/1 knapsack problem using a greedy algorithm. The function should take four parameters: `W` (the maximum weight capacity), `wt` (a list of weights for each item), `val` (a list of values for each item), and `n` (the number of items). The function should return the maximum total value that can be put in the knapsack.
"""

def knapSack(W, wt, val, n):
    knapsack = [0 for _ in range(W+1)]
    for i in range(W+1):
        for j in range(n):
            if wt[j] <= i:
                knapsack[i] = max(knapsack[i], knapsack[i-wt[j]]+val[j])
    return knapsack[W]