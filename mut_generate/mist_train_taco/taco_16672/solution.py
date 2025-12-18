"""
QUESTION:
# Task
 Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

 The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.

 ![](https://codefightsuserpics.s3.amazonaws.com/tasks/chessKnight/img/knight.jpg?_tm=1473533979951)

# Example

 For `cell = "a1"`, the output should be `2`.

 ![](https://codefightsuserpics.s3.amazonaws.com/tasks/chessKnight/img/ex_1.jpg?_tm=1473533980197)

 For `cell = "c2"`, the output should be `6`.

 ![](https://codefightsuserpics.s3.amazonaws.com/tasks/chessKnight/img/ex_2.jpg?_tm=1473533980368)

# Input/Output


 - `[input]` string `cell`

    String consisting of letter+number - coordinates of the knight on an 8 × 8 chessboard in chess notation.


 - `[output]` an integer
"""

def count_knight_moves(cell: str) -> int:
    # Convert the chess notation to board coordinates (0-based index)
    x, y = ord(cell[0]) - ord('a'), int(cell[1]) - 1
    
    # Possible moves for a knight
    moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    
    # Count valid moves
    valid_moves = 0
    for dx, dy in moves:
        if 0 <= x + dx < 8 and 0 <= y + dy < 8:
            valid_moves += 1
    
    return valid_moves