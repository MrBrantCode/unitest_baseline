"""
QUESTION:
You are in a grid of dimensions N \times M.

You are allowed to perform two types of operations:
Go down, left, up, or right each for a cost of X. Formally, if you are at the cell (i,j) of the grid, you can go to either of the cells (i + 1, j), (i, j - 1), (i - 1, j) or (i, j + 1) at a cost of X.
Go diagonally down-left, down-right, up-left, up-right, for a cost of Y. Formally, if you are at the cell (i,j) of the grid, you can go to either of the cells (i + 1, j - 1), (i + 1, j + 1), (i - 1, j - 1) or (i - 1, j + 1) at a cost of Y.

You cannot exit the grid at any point. Find the minimum cost of going to the bottom-right corner (N, M) from the top-left corner (1, 1). 

\textbf{Note}: Since input-output is large, prefer using fast input-output methods.

------ Input Format ------ 

- First line will contain T, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, four space separated integers integers: N, M, X, Y.

------ Output Format ------ 

For each testcase, output the answer in a new line.

------ Constraints ------ 

$1 ≤ T ≤ 5 \cdot 10^{5}$
$1 ≤ N, M, X, Y ≤ 10^{6}$

----- Sample Input 1 ------ 
3
5 6 2 5
4 7 5 6
7 8 6 5
----- Sample Output 1 ------ 
18
33
36
----- explanation 1 ------ 
Test Case $1$:
We can go $4$ steps down from $(1, 1)$ to $(5, 1)$ and then $5$ steps right to $(5, 6)$. The total cost is $2 \times 9 = 18$

Test Case $2$:
We can go $3$ steps diagonally down-right from $(1, 1)$ to $(4, 4)$ and then $3$ steps right to $(4, 7)$. The total cost is $3 \times 6 + 3 \times 5  = 18 + 15 = 33$

Test Case $3$:
We can go $6$ steps diagonally down-right from $(1, 1)$ to $(7, 7)$ and then $1$ step right to $(7, 8)$. The total cost is $5 \times 6 + 6 = 36$
"""

def calculate_minimum_cost(N, M, X, Y):
    """
    Calculate the minimum cost to move from the top-left corner (1, 1) to the bottom-right corner (N, M) in a grid.

    Parameters:
    N (int): Number of rows in the grid.
    M (int): Number of columns in the grid.
    X (int): Cost to move down, left, up, or right.
    Y (int): Cost to move diagonally.

    Returns:
    int: The minimum cost to reach the bottom-right corner from the top-left corner.
    """
    d = abs(M - N)
    path1 = X * (N - 1 + M - 1)
    path2 = Y * (min(N, M) - 1) + d * min(X, Y)
    if d % 2 and X >= Y:
        path2 += X - Y
    return min(path1, path2)