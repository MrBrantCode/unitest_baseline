"""
QUESTION:
# Introduction:

Reversi is a game usually played by 2 people on a 8x8 board.
Here we're only going to consider a single 8x1 row.

Players take turns placing pieces, which are black on one side and white on the
other, onto the board with their colour facing up.  If one or more of the
opponents pieces are sandwiched by the piece just played and another piece of
the current player's colour, the opponents pieces are flipped to the
current players colour.

Note that the flipping stops when the first piece of the player's colour is reached.

# Task:

Your task is to take an array of moves and convert this into a string
representing the state of the board after all those moves have been played.

# Input:

The input to your function will be an array of moves.
Moves are represented by integers from 0 to 7 corresponding to the 8 squares on the board.
Black plays first, and black and white alternate turns.
Input is guaranteed to be valid. (No duplicates, all moves in range, but array may be empty)

# Output:

8 character long string representing the final state of the board.
Use '*' for black and 'O' for white and '.' for empty.

# Examples:
```python
  reversi_row([])      # '........'
  reversi_row([3])     # '...*....'
  reversi_row([3,4])   # '...*O...'
  reversi_row([3,4,5]) # '...***..'
```
"""

def reversi_row(moves):
    row = '........'
    stones = '*O'
    for i, m in enumerate(moves):
        L, M, R = row[:m], stones[i % 2], row[m + 1:]
        
        # Check and flip stones to the right
        if R and R[0] == stones[(i + 1) % 2] and R.find(stones[i % 2]) > 0 and '.' not in R[:R.find(stones[i % 2])]:
            R = R.replace(stones[(i + 1) % 2], stones[i % 2], R.find(stones[i % 2]))
        
        # Check and flip stones to the left
        if L and L[-1] == stones[(i + 1) % 2] and L[::-1].find(stones[i % 2]) > 0 and '.' not in L[-1 - L[::-1].find(stones[i % 2]):]:
            L = L[::-1].replace(stones[(i + 1) % 2], stones[i % 2], L[::-1].find(stones[i % 2]))[::-1]
        
        row = L + M + R
    
    return row