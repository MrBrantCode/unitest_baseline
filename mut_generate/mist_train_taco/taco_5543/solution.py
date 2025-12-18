"""
QUESTION:
Two players are playing a game on a $15\times15$ chessboard. The rules of the game are as follows:

The game starts with $\boldsymbol{\mbox{k}}$ coins located at one or more $(x,y)$ coordinates on the board (a single cell may contain more than one coin). The coordinate of the upper left cell is $(1,1)$, and the coordinate of the lower right cell is $(15,15)$.

In each move, a player must move a single coin from some cell $(x,y)$ to one of the following locations:

$(x-2,y+1)$ 
$(x-2,y-1)$ 
$(x+1,y-2)$ 
$(x-1,y-2)$. 

Note: The coin must remain inside the confines of the board.

The players move in alternating turns. The first player who is unable to make a move loses the game.

The figure below shows all four possible moves:

Note: While the figure shows a $8\times8$ board, this game is played on a $15\times15$ board.

Given the value of $\boldsymbol{\mbox{k}}$ and the initial coordinate(s) of $\boldsymbol{\mbox{k}}$ coins, determine which player will win the game. Assume both players always move optimally.

Input Format

The first line contains an integer, $\mathbf{T}$, denoting the number of test cases. 

Each test case is defined as follows over the subsequent lines:

The first line contains an integer, $\boldsymbol{\mbox{k}}$, denoting the number of coins on the board.
Each line $\boldsymbol{i}$ (where $0\leq i<k$) of the $\boldsymbol{\mbox{k}}$ subsequent lines contains $2$ space-separated integers describing the respective values of $x_i$ and $y_i$ of the coordinate where coin $k_i$ is located.

Note: Recall that a cell can have more than one coin (i.e., any cell can have $0$ to $\boldsymbol{\mbox{k}}$ coins in it at any given time).

Constraints

$1\leq T\leq1000$
$1\leq k\leq1000$
$1\leq x_i,y_i\leq15$, where $0\leq i<k$.

Output Format

On a new line for each test case, print $\textbf{First}$ if the first player is the winner; otherwise, print $\textbf{Second}$.

Sample Input
2
3
5 4
5 8
8 2
6
7 1
7 2
7 3
7 4
7 4
7 4

Sample Output
First
Second
"""

def determine_winner(test_cases):
    grundy = [[-1] * 15 for _ in range(15)]
    grundy[0][0] = grundy[0][1] = grundy[1][0] = grundy[1][1] = 0

    def move_coin(x, y):
        if x > 1:
            if y > 0:
                yield (x - 2, y - 1)
            if y < 14:
                yield (x - 2, y + 1)
        if y > 1:
            if x > 0:
                yield (x - 1, y - 2)
            if x < 14:
                yield (x + 1, y - 2)

    def get_grundy(x, y):
        if grundy[x][y] != -1:
            return grundy[x][y]
        s = set()
        for (i, j) in move_coin(x, y):
            s.add(get_grundy(i, j))
        mex = 0
        while mex in s:
            mex += 1
        grundy[x][y] = mex
        return mex

    results = []
    for case in test_cases:
        k = case['k']
        coordinates = case['coordinates']
        coins = [[0] * 15 for _ in range(15)]
        for (i, j) in coordinates:
            coins[i - 1][j - 1] = 1 - coins[i - 1][j - 1]
        res = 0
        for i in range(15):
            for j in range(15):
                if coins[i][j]:
                    res ^= get_grundy(i, j)
        results.append('First' if res else 'Second')
    return results