"""
QUESTION:
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:


Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

def count_n_queens_solutions(n):
    def dfs(lst, xy_dif, xy_sum):
        p = len(lst)
        if p == n:
            res.append(lst)
            return
        for q in range(n):
            if q not in lst and p - q not in xy_dif and p + q not in xy_sum:
                dfs(lst + [q], xy_dif + [p - q], xy_sum + [p + q])
    
    res = []
    dfs([], [], [])
    return len(res)