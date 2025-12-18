"""
QUESTION:
Write a function `knapSack(W, wt, val, n)` that implements the Dynamic Programming approach to solve the 0-1 Knapsack Problem. The function should take four parameters: `W` (the total weight the knapsack can carry), `wt` (a list of weights of items), `val` (a list of profits associated with the items), and `n` (the number of items). The function should return the maximum total profit achievable within the given weight capacity.
"""

def knapSack(W, wt, val, n):
    K = [[0 for w in range(W+1)] for i in range(n+1)]

    # building K[][] in bottom-up manner:
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]