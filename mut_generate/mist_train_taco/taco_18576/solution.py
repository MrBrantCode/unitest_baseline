"""
QUESTION:
Consider some square matrix A with side n consisting of zeros and ones. There are n rows numbered from 1 to n from top to bottom and n columns numbered from 1 to n from left to right in this matrix. We'll denote the element of the matrix which is located at the intersection of the i-row and the j-th column as Ai, j.

Let's call matrix A clear if no two cells containing ones have a common side.

Let's call matrix A symmetrical if it matches the matrices formed from it by a horizontal and/or a vertical reflection. Formally, for each pair (i, j) (1 ≤ i, j ≤ n) both of the following conditions must be met: Ai, j = An - i + 1, j and Ai, j = Ai, n - j + 1.

Let's define the sharpness of matrix A as the number of ones in it.

Given integer x, your task is to find the smallest positive integer n such that there exists a clear symmetrical matrix A with side n and sharpness x.

Input

The only line contains a single integer x (1 ≤ x ≤ 100) — the required sharpness of the matrix.

Output

Print a single number — the sought value of n.

Examples

Input

4


Output

3


Input

9


Output

5

Note

The figure below shows the matrices that correspond to the samples:

<image>
"""

import math

def find_smallest_n_for_sharpness(x: int) -> int:
    def make_dp():
        dp = [0] * 1001
        dp[1] = 1
        dp[3] = 5
        for i in range(5, 100, 2):
            dp[i] = dp[i - 2] + i + i - 2
        return dp
    
    if x == 3:
        return 5
    
    dp = make_dp()
    for i in range(1, len(dp)):
        if x <= dp[i]:
            return i