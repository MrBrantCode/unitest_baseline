"""
QUESTION:
# Description

Write a function that accepts the current position of a knight in a chess board, it returns the possible positions that it will end up after 1 move. The resulted should be sorted. 

## Example

"a1" -> ["b3", "c2"]
"""

def get_knight_moves(position: str) -> list[str]:
    # Convert the position to row and column indices
    (r, c) = (ord(position[0]) - 96, int(position[1]))
    
    # Possible moves for a knight
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    
    # Generate possible new positions
    possible_positions = [''.join((chr(r + i + 96), str(c + j))) for (i, j) in moves 
                          if 1 <= r + i <= 8 and 1 <= c + j <= 8]
    
    # Sort the positions alphabetically
    possible_positions.sort()
    
    return possible_positions