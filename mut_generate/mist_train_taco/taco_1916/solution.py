"""
QUESTION:
The n-queens puzzle is the problem of placing n queens on a (n×n) chessboard such that no two queens can attack each other.
Given an integer n, find all distinct solutions to the n-queens puzzle. Each solution contains distinct board configurations of the n-queens’ placement, where the solutions are a permutation of [1,2,3..n] in increasing order, here the number in the ith place denotes that the ith-column queen is placed in the row with that number. For eg below figure represents a chessboard [3 1 4 2].
 
Example 1:
Input:
1
Output:
[1]
Explaination:
Only one queen can be placed 
in the single cell available.
Example 2:
Input:
4
Output:
[2 4 1 3 ] [3 1 4 2 ]
Explaination:
These are the 2 possible solutions.
 
Your Task:
You do not need to read input or print anything. Your task is to complete the function nQueen() which takes n as input parameter and returns a list containing all the possible chessboard configurations in sorted order. Return an empty list if no solution exists.
 
Expected Time Complexity: O(n!)
Expected Auxiliary Space: O(n^{2}) 
 
Constraints:
1 ≤ n ≤ 10
"""

def solve_n_queens(n):
    def is_safe(row, col, board):
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i][col]:
                return False
        
        # Check upper left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            i -= 1
            j -= 1
        
        # Check upper right diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j]:
                return False
            i -= 1
            j += 1
        
        return True

    def solve_queen(row, board, ans):
        if row == n:
            temp = []
            for r in range(n):
                for c in range(n):
                    if board[r][c] == 1:
                        temp.append(c + 1)
            ans.append(temp)
            return
        
        for col in range(n):
            if is_safe(row, col, board):
                board[row][col] = 1
                solve_queen(row + 1, board, ans)
                board[row][col] = 0

    board = [[0 for _ in range(n)] for _ in range(n)]
    ans = []
    solve_queen(0, board, ans)
    return ans