"""
QUESTION:
Implement a function `is_valid_move` that determines whether a given move is valid according to the rules of chess. The function takes as input a chessboard represented as an 8x8 grid and a move represented as a tuple of two tuples, where the first tuple is the starting position of the piece to be moved and the second tuple is the destination position. The chessboard is a list of lists where each piece is denoted by its initials and color ("w" for white, "b" for black). The function should return True if the move is valid and False otherwise. The move validation should only consider the rules for the piece being moved, without taking into account other pieces on the board that may be under attack or in a position to capture.
"""

def is_valid_move(chessboard, move):
    start_row, start_col = move[0]
    dest_row, dest_col = move[1]
    
    piece = chessboard[start_row][start_col]
    dest_piece = chessboard[dest_row][dest_col]
    
    if piece == 'P':  # Check for pawn move
        if start_col == dest_col:  # Moving forward
            if dest_piece == ' ':  # Destination is empty
                if start_row - dest_row == 1:  # Move by one square
                    return True
                elif start_row == 6 and start_row - dest_row == 2 and chessboard[start_row - 1][start_col] == ' ':  # Move by two squares from initial position
                    return True
            elif abs(start_col - dest_col) == 1 and start_row - dest_row == 1 and dest_piece.islower():  # Capture diagonally
                return True
        return False
    # Add similar checks for other pieces (Rook, Knight, Bishop, Queen, King)
    # ...
    else:
        return False  # Invalid piece