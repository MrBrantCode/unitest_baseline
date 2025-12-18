"""
QUESTION:
Write a function `knight_moves(x, y)` that returns all possible moves of a knight on a chessboard from the given position (x, y). The knight moves in an L-shape (two squares in one direction, then one square in a perpendicular direction).
"""

def knight_moves(x, y):
    result = []
    # Move 1 on x-axis, 2 on the y-axis 
    result.append((x + 1, y + 2)) 
    # Move 2 on x-axis, 1 on the y-axis
    result.append((x + 2, y + 1))
  
    # Move 1 on x-axis, -2 on the y-axis 
    result.append((x + 1, y - 2)) 
    # Move -2 on x-axis, 1 on the y-axis 
    result.append((x - 2, y + 1))
  
    # Move -1 on x-axis, 2 on the y-axis 
    result.append((x - 1, y + 2)) 
    # Move 2 on x-axis, -1 on the y-axis 
    result.append((x + 2, y - 1))
  
    # Move -1 on x-axis, -2 on the y-axis 
    result.append((x - 1, y - 2)) 
    # Move -2 on x-axis, -1 on the y-axis
    result.append((x - 2, y - 1)) 

    return result