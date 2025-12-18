"""
QUESTION:
Implement a function called `tictactoe` that simulates a game of Tic-Tac-Toe on a 5x5 grid. The function should take a 5x5 game board represented as a nested list of 'X', 'O', or ' ' (empty) cells and a string representing the symbol ('X' or 'O') of the player making the move. 

The function should return a tuple containing a boolean indicating whether the move is valid and a string indicating the outcome of the move. The function should check for valid moves, wins, draws, and out of bounds conditions, and it should enforce a rule where players can only make a move if their symbol matches the symbol in the center cell of the board. 

The function should also keep track of the number of moves made by each player and limit the maximum number of moves to 10 for each player. The time complexity of the function should be O(n^2), where n is the size of the grid.
"""

def tictactoe(board, symbol):
    # Validate the game board size
    if len(board) != 5 or any(len(row) != 5 for row in board):
        return (False, 'Invalid move: Invalid board size')
    
    # Validate the symbol in the center cell
    if board[2][2] != symbol:
        return (False, 'Invalid move: Symbol does not match center cell')
    
    # Count the number of moves made by each player
    count_X = sum(row.count('X') for row in board)
    count_O = sum(row.count('O') for row in board)
    
    # Check if either player has made more than 10 moves
    if count_X > 10 or count_O > 10:
        return (False, 'Invalid move: Maximum number of moves exceeded')
    
    # Check for a win condition
    if check_win(board, symbol):
        return (True, 'Valid move: Player {} wins'.format(symbol))
    
    # Check for a draw condition
    if count_X + count_O == 25:
        return (True, 'Valid move: Draw')
    
    # If none of the above conditions are met, the move is valid and the game is still in progress
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
    if all(board[i][i] == symbol for i in range(5)) or all(board[i][4-i] == symbol for i in range(5)):
        return True
    
    return False