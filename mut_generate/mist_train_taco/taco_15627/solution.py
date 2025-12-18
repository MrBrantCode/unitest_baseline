"""
QUESTION:
There are N items, numbered 1, 2, \ldots, N. For each i (1 \leq i \leq N), Item i has a weight of w_i and a value of v_i.

Taro has decided to choose some of the N items and carry them home in a knapsack. The capacity of the knapsack is W, which means that the sum of the weights of items taken must be at most W.

Find the maximum possible sum of the values of items that Taro takes home.

Constraints

* All values in input are integers.
* 1 \leq N \leq 100
* 1 \leq W \leq 10^9
* 1 \leq w_i \leq W
* 1 \leq v_i \leq 10^3

Input

Input is given from Standard Input in the following format:


N W
w_1 v_1
w_2 v_2
:
w_N v_N


Output

Print the maximum possible sum of the values of items that Taro takes home.

Examples

Input

3 8
3 30
4 50
5 60


Output

90


Input

1 1000000000
1000000000 10


Output

10


Input

6 15
6 5
5 6
6 4
6 6
3 5
7 2


Output

17
"""

def max_knapsack_value(N, W, items):
    # Initialize the dp array
    dp = [0] + [W + 1] * (N * 10 ** 3)
    
    # Iterate over each item
    for w, v in items:
        # Update the dp array in reverse order
        for j in range(N * 10 ** 3 + 1 - v)[::-1]:
            dp[j + v] = min(dp[j + v], dp[j] + w)
    
    # Find the maximum value where the weight is within the capacity
    for i in range(N * 10 ** 3 + 1)[::-1]:
        if dp[i] <= W:
            return i

    # If no valid solution is found, return 0 (though this should not happen given the constraints)
    return 0