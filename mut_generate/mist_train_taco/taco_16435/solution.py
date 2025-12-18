"""
QUESTION:
There are K items placed on a grid of squares with R rows and C columns. Let (i, j) denote the square at the i-th row (1 \leq i \leq R) and the j-th column (1 \leq j \leq C). The i-th item is at (r_i, c_i) and has the value v_i.
Takahashi will begin at (1, 1), the start, and get to (R, C), the goal. When he is at (i, j), he can move to (i + 1, j) or (i, j + 1) (but cannot move to a non-existent square).
He can pick up items on the squares he visits, including the start and the goal, but at most three for each row. It is allowed to ignore the item on a square he visits.
Find the maximum possible sum of the values of items he picks up.

-----Constraints-----
 - 1 \leq R, C \leq 3000
 - 1 \leq K \leq \min(2 \times 10^5, R \times C)
 - 1 \leq r_i \leq R
 - 1 \leq c_i \leq C
 - (r_i, c_i) \neq (r_j, c_j) (i \neq j)
 - 1 \leq v_i \leq 10^9
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
R C K
r_1 c_1 v_1
r_2 c_2 v_2
:
r_K c_K v_K

-----Output-----
Print the maximum possible sum of the values of items Takahashi picks up.

-----Sample Input-----
2 2 3
1 1 3
2 1 4
1 2 5

-----Sample Output-----
8

He has two ways to get to the goal:
 - Visit (1, 1), (1, 2), and (2, 2), in this order. In this case, the total value of the items he can pick up is 3 + 5 = 8.
 - Visit (1, 1), (2, 1), and (2, 2), in this order. In this case, the total value of the items he can pick up is 3 + 4 = 7.
Thus, the maximum possible sum of the values of items he picks up is 8.
"""

def max_item_value_sum(R, C, items):
    # Initialize DP tables
    dp1 = [[0] * (C + 1) for _ in range(R + 1)]
    dp2 = [[0] * (C + 1) for _ in range(R + 1)]
    dp3 = [[0] * (C + 1) for _ in range(R + 1)]
    
    # Place items in the grid
    for r, c, v in items:
        dp1[r][c] = v
    
    # Fill DP tables
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            a = dp1[i][j]
            dp3[i][j] = max(dp2[i][j - 1] + a, dp3[i][j - 1])
            dp2[i][j] = max(dp1[i][j - 1] + a, dp2[i][j - 1])
            dp1[i][j] = max(dp1[i - 1][j] + a, dp2[i - 1][j] + a, dp3[i - 1][j] + a, dp1[i][j - 1], a)
    
    # Return the maximum possible sum
    return max(dp1[R][C], dp2[R][C], dp3[R][C])