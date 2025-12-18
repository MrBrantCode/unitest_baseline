"""
QUESTION:
Programmers generally love to play chess! You too have recently acquired an interest in playing chess and you find bishop to be the most fascinating warrior of all. During a random chess practice session, you are faced with this problem : 

"Two bishops are lying on the chessboard. You can move only one of them. What is the minimum number of moves required to put the two bishops in an attacking position? "

Here, a move is equivalent to moving the bishop diagonally on the chess board. If the answer is greater than or equal to 10^15, output -1.

Input Format

First line contains T , the number of test cases. Each of the next "T" lines contains X1 Y1 X2 Y2, denoting the positions of the two bishops on the chessboard.

Output Format

For each of the T test cases, output the answer as required.

Constraints

**1 ≤ T ≤ 10^5

1 ≤ X1 , X2 , Y1 , Y2 ≤ 8**

SAMPLE INPUT
2
1 1 1 2
2 2 3 3

SAMPLE OUTPUT
-1
0
"""

def min_moves_to_attack(x1: int, y1: int, x2: int, y2: int) -> int:
    """
    Calculate the minimum number of moves required to put two bishops in an attacking position on a chessboard.

    Parameters:
    x1 (int): The x-coordinate of the first bishop.
    y1 (int): The y-coordinate of the first bishop.
    x2 (int): The x-coordinate of the second bishop.
    y2 (int): The y-coordinate of the second bishop.

    Returns:
    int: The minimum number of moves required. Returns -1 if the answer is greater than or equal to 10^15.
    """
    
    # Check if the positions are within the valid range of the chessboard
    if any(x > 8 or x < 1 for x in [x1, x2, y1, y2]):
        return -1

    # Check if the bishops are already on the same diagonal
    if abs(x1 - x2) == abs(y1 - y2):
        return 0

    # Determine the color of the squares the bishops are on
    C = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0],
    ]

    # Check if the bishops are on squares of different colors
    if C[x1][y1] != C[x2][y2]:
        return -1

    # If the bishops are on squares of the same color but not on the same diagonal
    return 1