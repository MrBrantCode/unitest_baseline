"""
QUESTION:
Create a function called `knapSack` that takes in four parameters: `max_weight`, `weights`, `values`, and `n`. The function should solve the knapsack problem by determining the maximum total value of items that can be chosen without exceeding the `max_weight`. The function should use dynamic programming and return the maximum total value. 

Restrictions: The `weights` and `values` are lists of integers, `max_weight` is an integer, and `n` is the number of items (equal to the length of `weights` and `values`).
"""

def knapSack(max_weight, weights, values, n):
    K = [[0 for w in range(max_weight+1)] for i in range(n+1)]
    
    for i in range(n+1):
        for w in range(max_weight+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i-1] <= w:
                K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][max_weight]