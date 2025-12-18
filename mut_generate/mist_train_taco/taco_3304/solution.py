"""
QUESTION:
Based on [this kata, Connect Four.](https://www.codewars.com/kata/connect-four-1)

In this kata we play a modified game of connect four. It's connect X, and there can be multiple players.

Write the function ```whoIsWinner(moves,connect,size)```.

```2 <= connect <= 10```

```2 <= size <= 52```

Each column is identified by a character, A-Z a-z:  
``` ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ```


Moves come in the form:

```
['C_R','p_Y','s_S','I_R','Z_Y','d_S']
```
* Player R puts on C
* Player Y puts on p
* Player S puts on s
* Player R puts on I
* ...

The moves are in the order that they are played. 

The first player who connect ``` connect ``` items in same color is the winner. 

Note that a player can win before all moves are done. You should return the first winner.

If no winner is found, return "Draw".

A board with size 7, where yellow has connected 4:

All inputs are valid, no illegal moves are made.

![alt text](https://i.imgur.com/xnJEsIx.png)
"""

from itertools import compress
from string import ascii_uppercase, ascii_lowercase

# Mapping of column characters to their respective indices
D = {c: i for (i, c) in enumerate(ascii_uppercase + ascii_lowercase)}

def determine_winner(moves, connect, size):
    def gen(i, j):
        """Generator to yield possible directions for checking consecutive pieces."""
        for x in range(1, connect):
            yield ((i, j - x), (i - x, j), (i + x, j), (i - x, j - x), (i + x, j + x), (i + x, j - x), (i - x, j + x))

    def check(i, j, p):
        """Check if the current move results in a win."""
        (memo, count) = ([True] * 7, [0] * 7)
        for L in gen(i, j):
            for (x, (k, l)) in enumerate(L):
                memo[x] = memo[x] and 0 <= k < size and (0 <= l < size) and (grid[k][l] == p)
                count[x] += memo[x]
            if not any(memo):
                return max(count[0], count[1] + count[2], count[3] + count[4], count[5] + count[6]) + 1 >= connect
        return True

    # Initialize the grid
    grid = [[None] * size for _ in range(size)]

    # Process each move
    for move in moves:
        i, p = D[move[0]], move[-1]
        j = next((j for j, x in enumerate(grid[i]) if x is None))
        if check(i, j, p):
            return p
        grid[i][j] = p

    return 'Draw'