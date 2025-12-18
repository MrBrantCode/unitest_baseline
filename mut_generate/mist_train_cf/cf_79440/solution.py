"""
QUESTION:
Write a function `validTicTacToe(board)` that takes a 3x3 Tic-Tac-Toe board as input, where each cell is either 'X', 'O', or ' '. Return True if the board represents a valid Tic-Tac-Toe game state and False otherwise. A valid state is one that could be reached by players taking turns placing 'X' and 'O' in empty spaces, with the game ending when there are three of the same character in a row, column, or diagonal, or when all spaces are filled. 

Note: `board` is a length-3 array of strings, where each string `board[i]` has length 3. Each `board[i][j]` is a character in the set {' ', 'X', 'O'}.
"""

def validTicTacToe(board):
    def iswin(player):
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):  # Row win
                return True
            if all(board[j][i] == player for j in range(3)):  # Column win
                return True
        if board[0][0] == board[1][1] == board[2][2] == player:  # Diagonal win 
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:  # Diagonal win 
            return True
        return False

    first, second = 'X', 'O'
    first_count = sum(row.count(first) for row in board)
    second_count = sum(row.count(second) for row in board)

    if first_count < second_count or first_count - second_count > 1:  # Invalid X and O count
        return False
    if iswin(first) and first_count == second_count:  # If X wins, there should be one X more than O
        return False
    if iswin(second) and first_count > second_count:  # If O wins, amount of X and O should be equal
        return False

    return True