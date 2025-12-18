"""
QUESTION:
# Task
 In the Land Of Chess, bishops don't really like each other. In fact, when two bishops happen to stand on the same diagonal, they immediately rush towards the opposite ends of that same diagonal.

 Given the initial positions (in chess notation) of two bishops, `bishop1` and `bishop2`, calculate their future positions. Keep in mind that bishops won't move unless they see each other along the same diagonal.

# Example

 For `bishop1 = "d7" and bishop2 = "f5"`, the output should be `["c8", "h3"]`.

 ![](https://codefightsuserpics.s3.amazonaws.com/tasks/bishopDiagonal/img/ex_1.jpg?_tm=1473766087137)

 For `bishop1 = "d8" and bishop2 = "b5"`, the output should be `["b5", "d8"]`.

 The bishops don't belong to the same diagonal, so they don't move.

 ![](https://codefightsuserpics.s3.amazonaws.com/tasks/bishopDiagonal/img/ex_2.jpg?_tm=1473766087425)

# Input/Output


 - `[input]` string `bishop1`

    Coordinates of the first bishop in chess notation.


 - `[input]` string `bishop2`

    Coordinates of the second bishop in the same notation.


 - `[output]` a string array

    Coordinates of the bishops in lexicographical order after they check the diagonals they stand on.
"""

def calculate_bishop_positions(bishop1, bishop2):
    def chess_to_coords(pos):
        """Convert chess notation to coordinates."""
        return ['abcdefgh'.index(pos[0]), '12345678'.index(pos[1])]
    
    def coords_to_chess(coords):
        """Convert coordinates back to chess notation."""
        return 'abcdefgh'[coords[0]] + '12345678'[coords[1]]
    
    # Convert positions to coordinates
    a, b = sorted([chess_to_coords(bishop1), chess_to_coords(bishop2)])
    
    # Check if bishops are on the same diagonal
    m = int((b[1] - a[1]) / (b[0] - a[0])) if abs(a[1] - b[1]) == abs(a[0] - b[0]) else 0
    
    if m:
        # Move bishops to the edges of the board
        while all(0 < e < 7 for e in a):
            a = [a[0] - 1, a[1] - m]
        while all(0 < e < 7 for e in b):
            b = [b[0] + 1, b[1] + m]
    
    # Convert coordinates back to chess notation
    return sorted([coords_to_chess(a), coords_to_chess(b)])