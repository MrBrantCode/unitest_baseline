"""
QUESTION:
Toastman came up with a very easy task. He gives it to Appleman, but Appleman doesn't know how to solve it. Can you help him?

Given a n × n checkerboard. Each cell of the board has either character 'x', or character 'o'. Is it true that each cell of the board has even number of adjacent cells with 'o'? Two cells of the board are adjacent if they share a side.


-----Input-----

The first line contains an integer n (1 ≤ n ≤ 100). Then n lines follow containing the description of the checkerboard. Each of them contains n characters (either 'x' or 'o') without spaces.


-----Output-----

Print "YES" or "NO" (without the quotes) depending on the answer to the problem.


-----Examples-----
Input
3
xxo
xox
oxx

Output
YES

Input
4
xxxo
xoxo
oxox
xxxx

Output
NO
"""

def is_even_adjacent_o_checkerboard(n, board):
    def count_adjacent_o(i, j):
        count = 0
        if i > 0 and board[i-1][j] == 'o':  # Above
            count += 1
        if i < n-1 and board[i+1][j] == 'o':  # Below
            count += 1
        if j > 0 and board[i][j-1] == 'o':  # Left
            count += 1
        if j < n-1 and board[i][j+1] == 'o':  # Right
            count += 1
        return count

    for i in range(n):
        for j in range(n):
            if count_adjacent_o(i, j) % 2 != 0:
                return "NO"
    return "YES"