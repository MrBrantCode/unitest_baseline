"""
QUESTION:
A Tic-Tac-Toe board is given after some moves are played. Find out if the given board is valid, i.e., is it possible to reach this board position after some moves or not.
Note that every arbitrary filled grid of 9 spaces isn’t valid e.g. a grid filled with 3 X and 6 O isn’t valid situation because each player needs to take alternate turns.
Note :  The game starts with X
Example 1:
Input:
board[] = {'X', 'X', 'O', 
           'O', 'O', 'X',
           'X', 'O', 'X'};
Output: Valid
Explanation: This is a valid board.
Example 2:
Input:
board[] = {'O', 'X', 'X', 
           'O', 'X', 'X',
           'O', 'O', 'X'};
Output: Invalid
Explanation: Both X and O cannot win.
Your Task:
You don't need to read input or print anything. Your task is to complete the function isValid() which takes a character array of size 9 representing the board as input parameter and returns a boolean value denoting if it is valid or not.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
Every character on the board can either be 'X' or 'O'.
"""

def is_valid_tic_tac_toe(board):
    # Check if the board has exactly 9 elements
    if len(board) != 9:
        return False
    
    # Count the number of 'X' and 'O'
    count_X = board.count('X')
    count_O = board.count('O')
    
    # The number of 'X' should be equal to or one more than the number of 'O'
    if not (count_X == count_O or count_X == count_O + 1):
        return False
    
    # Check for winning conditions for 'X' and 'O'
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    
    x_wins = False
    o_wins = False
    
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c]:
            if board[a] == 'X':
                x_wins = True
            elif board[a] == 'O':
                o_wins = True
    
    # Both 'X' and 'O' cannot win simultaneously
    if x_wins and o_wins:
        return False
    
    # If 'O' wins, the number of 'X' should be equal to the number of 'O'
    if o_wins and count_X != count_O:
        return False
    
    # If 'X' wins, the number of 'X' should be one more than the number of 'O'
    if x_wins and count_X != count_O + 1:
        return False
    
    return True