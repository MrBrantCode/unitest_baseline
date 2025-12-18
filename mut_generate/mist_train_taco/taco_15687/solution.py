"""
QUESTION:
## Decode the diagonal. 

Given a grid of characters. Output a decoded message as a string.

Input

```
  H Z R R Q
  D I F C A E A !
  G H T E L A E 
  L M N H P R F 
  X Z R P E
```
  
Output

`HITHERE!` (diagonally down right `↘` and diagonally up right `↗` if you can't go further).

The message ends when there is no space at the right up or down diagonal.

To make things even clearer: the same example, but in a simplified view

```
  H _ _ _ _
  _ I _ _ _ _ _ !
  _ _ T _ _ _ E 
  _ _ _ H _ R _
  _ _ _ _ E
```
"""

def decode_diagonal_message(grid: str) -> str:
    # Convert the grid string into a list of lists of characters
    grid = [line.split() for line in grid.split('\n')]
    
    # Initialize starting position, direction, and the resulting message
    i, j, d, message = 0, 0, 1, ''
    
    # Traverse the grid diagonally
    while 0 <= i < len(grid) and j < len(grid[i]):
        if 0 <= j < len(grid[i]):
            message += grid[i][j]
            i, j = i + d, j + 1
        else:
            i += d
        
        # Change direction if we hit the top or bottom boundary
        if i == 0 or i == len(grid) - 1:
            d = -d
    
    return message