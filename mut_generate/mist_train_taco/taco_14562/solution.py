"""
QUESTION:
Bob is playing a popular game called "Dungeon". The game is played on a rectangular board consisting of W × H squares. Each square is identified with its column and row number, thus the square located in the x-th column and the y-th row is represented as (x, y). The left-most square in the top row is (0, 0) and the right-most square in the bottom row is (W-1, H-1).

Bob moves a character "BomBom" to clear the game. BomBom is initially located at (0, 0). The game is won if Bob successfully destroys all the enemy characters on the board by manipulating BomBom cleverly. The enemy characters are fixed on specific squares, and Bob can manipulate BomBom using the following two operations any number of times.

* One-square movement in the up, down, left, or right direction within the board
* Using a bomb, eliminate all the enemy characters that are located in the same column and row as that of BomBom



BomBom consumes a Cost when it moves from one square to another. BomBom can use a bomb any number of times without consuming a Cost. Use of a bomb has no effect on BomBom’s behavior and it can move even to a square where an enemy character is located.

Given the board size and enemy information, make a program to evaluate the minimum Cost BomBom consumes before it destroys all enemy characters.



Input

The input is given in the following format.


W H N
x_1 y_1
x_2 y_2
:
x_N y_N


The first line provides the number of squares in the horizontal direction W (1 ≤ W ≤ 105), in the vertical direction H (1 ≤ H ≤ 105), and the number of enemy characters N (1 ≤ N ≤ 105). Each of the subsequent N lines provides location information of the i-th enemy, column x_i (0 ≤ x_i ≤ W-1) and row y_i (0 ≤ y_i ≤ H-1). The number of enemy characters in a specific square can be either one or zero.

Output

Output the minimum Cost in a line.

Examples

Input

5 4 4
0 3
1 1
2 2
2 3


Output

2


Input

6 6 5
2 1
5 2
3 3
1 4
1 5


Output

4


Input

8 8 4
6 0
7 0
0 6
0 7


Output

0
"""

def calculate_minimum_cost(W: int, H: int, enemies: list) -> int:
    """
    Calculate the minimum cost BomBom consumes before it destroys all enemy characters on the board.

    Parameters:
    - W (int): The number of squares in the horizontal direction (width of the board).
    - H (int): The number of squares in the vertical direction (height of the board).
    - enemies (list): A list of tuples where each tuple contains the coordinates (x, y) of an enemy character.

    Returns:
    - int: The minimum cost BomBom consumes.
    """
    n = len(enemies)
    if n == 0:
        return 0
    
    # Sort enemies by their x-coordinate
    enemies.sort()
    
    # Calculate the maximum y-coordinate for enemies from the end to the start
    y_max = [0]
    for _, y in reversed(enemies):
        y_max.append(max(y_max[-1], y))
    
    # Extract x-coordinates of enemies and add the starting point (0, 0)
    xs = [0] + [x for x, _ in enemies]
    
    # Calculate the minimum cost
    min_cost = min([xs[i] + y_max[n - i] for i in range(n + 1)])
    
    return min_cost