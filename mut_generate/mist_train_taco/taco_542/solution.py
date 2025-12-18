"""
QUESTION:
Matrix of given integers


a1,1 a1,2 ... a1, n
a2,1 a2,2 ... a2, n
::
an, 1 an, 2 ... an, n


Then, create a program that outputs the maximum value of the sum of one or more consecutive terms (submatrix) in the vertical and horizontal directions and ends.



Input

The input data is given in the following format.


n
a1,1 a1,2 ... a1, n
a2,1 a2,2 ... a2, n
::
an, 1 an, 2 ... an, n


n is 1 or more and 100 or less, and ai, j is -10000 or more and 10000 or less.

Output

Print the maximum value on one line.

Examples

Input

3
1 -2 3
-4 5 6
7 8 -9


Output

16


Input

4
1 3 -9 2
2 7 -1 5
-8 3 2 -1
5 0 -3 1


Output

15
"""

def find_max_submatrix_sum(matrix, n):
    # Initialize the prefix sum matrix
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    # Fill the prefix sum matrix
    for r in range(n):
        for c in range(n):
            s[r + 1][c + 1] = matrix[r][c] + s[r][c + 1]
    
    # Initialize the answer to a very small number
    ans = -10001
    
    # Calculate the maximum submatrix sum
    for r_end in range(1, n + 1):
        for r_start in range(r_end):
            dp = [-10001]
            for c in range(1, n + 1):
                s_tmp = s[r_end][c] - s[r_start][c]
                dp.append(max(dp[c - 1] + s_tmp, s_tmp))
            ans = max(ans, max(dp))
    
    return ans