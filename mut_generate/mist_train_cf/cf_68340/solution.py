"""
QUESTION:
Write a function `totalNQueens(n)` to calculate the number of unique solutions to the n-queens puzzle, given an integer `n` representing the size of the chessboard. The function should return the total count of unique solutions where no pair of queens can attack each other. The input `n` is restricted to `1 <= n <= 9`.
"""

def totalNQueens(n):
    def DFS(queens, xy_diff, xy_sum):
        p = len(queens)
        if p==n:
            result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p-q not in xy_diff and p+q not in xy_sum: 
                DFS(queens+[q], xy_diff+[p-q], xy_sum+[p+q])  

    result = []
    DFS([], [], [])
    return len(result)