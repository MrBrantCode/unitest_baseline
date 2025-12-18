"""
QUESTION:
You are given a chessboard of size NxN. There is a white knight and several black pawns located on the board. The knight can move similarly to the normal knight in the game of chess; however it can only move towards the right of the board (see the below figure).

The mission of the knight is to capture as many black pawns as possible. Its journey ends when it moves to the rightmost column of the board.
Compute the maximum number of black pawns the white knight can capture.

------ Input ------ 

The first line contains t, the number of test cases (about 10). Then t test cases follow.
Each test case has the following form:
The first line contains N, the size of the chessboard (4 ≤ N ≤ 1000).
Then N lines follow, each line containing N characters which may be '.', 'K' or 'P', corresponding to the empty cell, the white knight, and the black pawn, respectively. There is exactly one 'K' character in the whole of the board.

------ Output ------ 

For each test case, print in a single line the maximum number of black pawns that can be captured.

----- Sample Input 1 ------ 
1
5
K....
..P..
.P...
...P.
.....
----- Sample Output 1 ------ 
2
"""

def max_pawns_captured(board, knight_pos, n):
    def maxpawns(x, y):
        if x >= n or x < 0 or y >= n:
            return 0
        if values[y][x] != -1:
            return values[y][x]
        values[y][x] = board[y][x] + max(
            maxpawns(x - 1, y + 2),
            maxpawns(x + 1, y + 2),
            maxpawns(x + 2, y + 1),
            maxpawns(x - 2, y + 1)
        )
        return values[y][x]

    # Initialize the values array
    values = [[-1] * n for _ in range(n)]
    
    # Convert board to numerical values
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                board[i][j] = 0
            elif board[i][j] == 'P':
                board[i][j] = 1
            else:
                board[i][j] = 0
    
    # Extract knight's initial position
    x1, y1 = knight_pos
    
    # Calculate the maximum pawns captured
    return maxpawns(x1, y1)