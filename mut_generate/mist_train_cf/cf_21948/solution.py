"""
QUESTION:
Write a function `tictactoe(board, symbol)` that simulates a move in a 5x5 Tic-Tac-Toe game. 

The function takes a 5x5 nested list `board` representing the current state of the game, where each element is 'X', 'O', or ' ' (empty), and a string `symbol` ('X' or 'O') representing the player making the move. 

The function returns a tuple containing a boolean indicating whether the move is valid and a string indicating the outcome of the move, which can be 'Valid move: Game in progress', 'Valid move: Player X/O wins', 'Valid move: Draw', 'Invalid move: Cell already occupied', or 'Invalid move: Out of bounds'.
"""

def entrance(board, symbol, row, col):
    # Check if the move is out of bounds
    if len(board) != 5 or any(len(row) != 5 for row in board) or row < 0 or row > 4 or col < 0 or col > 4:
        return (False, 'Invalid move: Out of bounds')
    
    # Check if the move is in an already occupied cell
    if board[row][col] != ' ':
        return (False, 'Invalid move: Cell already occupied')
    
    # Make the move
    board[row][col] = symbol
    
    # Check if the move resulted in a win
    if check_win(board, symbol):
        return (True, 'Valid move: Player {} wins'.format(symbol))
    
    # Check if the move resulted in a draw
    if check_draw(board):
        return (True, 'Valid move: Draw')
    
    # The move is valid and the game is still in progress
    return (True, 'Valid move: Game in progress')


def check_win(board, symbol):
    # Check rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    
    # Check columns
    for col in range(5):
        if all(board[row][col] == symbol for row in range(5)):
            return True
    
    # Check diagonals
    if all(board[i][i] == symbol for i in range(5)):
        return True
    if all(board[i][4-i] == symbol for i in range(5)):
        return True
    
    return False


def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True