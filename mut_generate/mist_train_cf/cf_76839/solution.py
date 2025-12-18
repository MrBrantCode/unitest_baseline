"""
QUESTION:
Design a function `knapSack(W, wt, val, n)` to solve the 0/1 Knapsack problem. Given the weights (`wt`) and values (`val`) of `n` items, and a maximum weight limit (`W`), return the maximum total value that can be put in a knapsack without exceeding the weight limit. Use memoization and dynamic programming to optimize the solution, avoiding redundant calculations and achieving a time complexity of O(n*W).
"""

def knapSack(W, wt, val, n):
    # First we will initialize a memoization matrix
    # Dimensions: n+1 (to account for zero items) by W+1 (to account for zero weight)
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]
 
    # We fill our memoization table (K) in bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            # If we have no items or no weight remaining, the value will be 0
            if i == 0 or w == 0:
                K[i][w] = 0
            # If our item's weight is less than or equal to remaining weight
            elif wt[i-1] <= w:
                # Compare incorporating that item or not
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            # If our item's weight is more than we have left, we can't add it
            else:
                K[i][w] = K[i-1][w]

    # The value in the bottom right represents the maximum value we can achieve
    return K[n][W]