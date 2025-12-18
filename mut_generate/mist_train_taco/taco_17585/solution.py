"""
QUESTION:
Tic-Tac-Toe used to be Chef's favourite game during his childhood. Reminiscing in his childhood memories, he decided to create his own "Tic-Tac-Toe", with rules being similar to the original Tic-Tac-Toe, other than the fact that it is played on an NxN board.

The game is played between two players taking turns. First player puts an 'X' in an empty cell of the board, then the second player puts an 'O' in some other free cell. If the first player has K continuous X's or the second player has K continuous O's in row, column or diagonal, then he wins.

Chef started playing this new "Tic-Tac-Toe" with his assistant, beginning as the first player himself (that is, Chef plays 'X's). Currently, the game is ongoign, and it's Chef's turn. However, he needs to leave soon to begin tonight's dinner preparations, and has time to play only one more move. If he can win in one move, output "YES", otherwise output "NO" (without quotes). It is guaranteed that no player has already completed the winning criterion before this turn, and that it's a valid "Tic-Tac-Toe" game.

-----Input-----
The first line of input contains one integer T denoting the number of testcases. First line of each testcase contains two integers N and K, next N lines contains N characters each. Each character is either an 'X' denoting that the first player used this cell, an 'O' meaning that the second player used this cell, or a '.' (a period) representing a free cell.

-----Output-----
For each testcase, output, in a single line, "YES" if Chef can win in one move, or "NO" otherwise.

-----Constraints-----
- 1 ≤ T ≤ 100
- 3 ≤ N ≤ 20
- 1 ≤ K ≤ N

-----Example-----
Input:
3
3 3
XOX
O.O
XOX
3 1
...
...
...
3 2
...
...
...

Output:
YES
YES
NO

Input:
1
4 4
XOXO
OX..
XO..
OXOX

Output:
YES

-----Subtasks-----
- Subtask 1:  K  = 1. Points - 10
- Subtask 2:  N  =  K  = 3. Points - 30
- Subtask 3: Original constraints. Points - 60

-----Explanation-----
Test #1:

In first testcase, put 'X' in (2, 2), in second we can put 'X' in any cell and win. 
Test #2:

If you put an 'X' in (3, 3), there will be four 'X's on the main diagonal (1, 1) - (2, 2) - (3, 3) - (4, 4).
"""

def can_chef_win_in_one_move(board, N, K):
    """
    Determines if Chef can win in one move in a Tic-Tac-Toe game on an NxN board with a winning length of K.

    Parameters:
    board (list of list of str): The NxN board configuration where each cell is 'X', 'O', or '.'.
    N (int): The size of the board (NxN).
    K (int): The length of continuous 'X's or 'O's required to win.

    Returns:
    bool: True if Chef can win in one move, False otherwise.
    """
    # Convert board to numerical representation for easier processing
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                board[i][j] = 1
            elif board[i][j] == '.':
                board[i][j] = 0
            else:
                board[i][j] = -1

    # Check rows and columns
    for i in range(N):
        for j in range(N - K + 1):
            if sum(board[i][j:j + K]) >= K - 1:
                return True
            col_sum = sum(board[x][i] for x in range(j, j + K))
            if col_sum >= K - 1:
                return True

    # Check diagonals
    for i in range(N - K + 1):
        main_diag_sum = sum(board[i + x][i + x] for x in range(K))
        anti_diag_sum = sum(board[i + x][N - i - x - 1] for x in range(K))
        if main_diag_sum >= K - 1 or anti_diag_sum >= K - 1:
            return True

    return False