"""
QUESTION:
Let us consider a grid of squares with 10^9 rows and N columns. Let (i, j) be the square at the i-th column (1 \leq i \leq N) from the left and j-th row (1 \leq j \leq 10^9) from the bottom.

Snuke has cut out some part of the grid so that, for each i = 1, 2, ..., N, the bottom-most h_i squares are remaining in the i-th column from the left. Now, he will paint the remaining squares in red and blue. Find the number of the ways to paint the squares so that the following condition is satisfied:

* Every remaining square is painted either red or blue.
* For all 1 \leq i \leq N-1 and 1 \leq j \leq min(h_i, h_{i+1})-1, there are exactly two squares painted red and two squares painted blue among the following four squares: (i, j), (i, j+1), (i+1, j) and (i+1, j+1).



Since the number of ways can be extremely large, print the count modulo 10^9+7.

Constraints

* 1 \leq N \leq 100
* 1 \leq h_i \leq 10^9

Input

Input is given from Standard Input in the following format:


N
h_1 h_2 ... h_N


Output

Print the number of the ways to paint the squares, modulo 10^9+7.

Examples

Input

9
2 3 5 4 1 2 4 2 1


Output

12800


Input

2
2 2


Output

6


Input

5
2 1 2 1 2


Output

256


Input

9
27 18 28 18 28 45 90 45 23


Output

844733013
"""

def count_painting_ways(N, heights):
    mod = 10**9 + 7
    heights.append(1)  # Append a dummy height to simplify the loop
    dp = [0] * (N + 1)
    
    # Initialize the first column
    ret = pow(2, heights[0], mod)
    for kk in range(N + 1):
        if heights[0] >= heights[kk]:
            dp[kk] = pow(2, heights[0] - heights[kk], mod) * 2
        else:
            dp[kk] = 2
    
    # Fill the dp array for each column
    for k in range(1, N):
        new_dp = [0] * (N + 1)
        for i in range(N + 1):
            if heights[i] <= heights[k]:
                if heights[k - 1] <= heights[i]:
                    new_dp[i] = dp[i] * 2 * pow(2, heights[k] - heights[i], mod)
                elif heights[k - 1] > heights[k]:
                    new_dp[i] = dp[i] - dp[k] + dp[k] * 2
                else:
                    new_dp[i] = (dp[i] - dp[k - 1] + dp[k - 1] * 2) * pow(2, heights[k] - heights[k - 1], mod)
            else:
                new_dp[i] = dp[k] * 2
            new_dp[i] %= mod
        dp = new_dp
    
    return dp[-1]