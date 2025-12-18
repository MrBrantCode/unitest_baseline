"""
QUESTION:
Two players are playing a game on a $15\times15$ chessboard. The rules of the game are as follows:

The game starts with a single coin located at some $x,y$ coordinates. The coordinates of the upper left cell are $(1,1)$, and of the lower right cell are $(15,15)$.

In each move, a player must move the coin from cell $(x,y)$ to one of the following locations:

$(x-2,y+1)$ 
$(x-2,y-1)$ 
$(x+1,y-2)$ 
$(x-1,y-2)$

Note: The coin must remain inside the confines of the board.

Beginning with player 1, the players alternate turns. The first player who is unable to make a move loses the game.

The figure below shows all four possible moves using an $8\times8$ board for illustration:

Given the initial coordinates of the players' coins, assuming optimal play, determine which player will win the game. 

Function Description

Complete the chessboardGame function in the editor below.  It should return a string, either First or Second.

chessboardGame has the following parameter(s):  

x: an integer that represents the starting column position   
y: an integer that represents the starting row position  

Input Format

The first line contains an integer $\boldsymbol{\boldsymbol{t}}$, the number of test cases. 

Each of the next $\boldsymbol{\boldsymbol{t}}$ lines contains $2$ space-separated integers $\boldsymbol{x}$ and $y$.

Constraints

$1\leq t\leq225$
$1\leq x[i],y[i]\leq15$

Output Format

On a new line for each test case, print $\textbf{First}$ if the first player is the winner.  Otherwise, print $\textbf{Second}$.

Sample Input
3
5 2
5 3
8 8

Sample Output
Second
First
First

Explanation

In the first case, player1 starts at the red square and can move to any of the blue squares.  Regardless of which one is chosen, the player 2 can move to one of the green squares to win the game.

In the second case, player 1 starts at the red square and can move to any of the blue squares or the purple one.  Moving to the purple one limits player 2 to the yellow square.  From the yellow square, player 1 moves to the green square and wins.
"""

def chessboard_game(x, y):
    # Possible moves
    moves = [(-2, 1), (-2, -1), (1, -2), (-1, -2)]
    
    # Initialize sets for winning positions
    First = set()
    Second = set()
    
    # Create a set of all possible positions on the 15x15 grid
    grid_copy = {(i, j) for i in range(1, 16) for j in range(1, 16)}
    
    # Determine winning positions
    t = 0
    while len(First) + len(Second) != 225:
        if t % 2 == 0:
            for (i, j) in grid_copy:
                n = 0
                for (dx, dy) in moves:
                    if (i + dx, j + dy) not in grid_copy or (i + dx, j + dy) in First:
                        n += 1
                if n == 4:
                    Second.add((i, j))
        else:
            for (i, j) in grid_copy:
                for (dx, dy) in moves:
                    if (i + dx, j + dy) in Second:
                        First.add((i, j))
        t += 1
    
    # Determine the winner based on the initial position
    if (x, y) in First:
        return "First"
    else:
        return "Second"