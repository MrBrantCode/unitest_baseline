"""
QUESTION:
Remember the game 2048?

The main part of this game is merging identical tiles in a row. 

* Implement a function that models the process of merging all of the tile values in a single row.  
* This function takes the array line as a parameter and returns a new array with the tile values from line slid towards the front of the array (index 0) and merged.
* A given tile can only merge once.
* Empty grid squares are represented as zeros.
* Your function should work on arrays containing arbitrary number of elements.


## Examples

```
merge([2,0,2,2])  -->  [4,2,0,0]
```

Another example with repeated merges: 

```
merge([4,4,8,16])  -->  [8,8,16,0]
merge([8,8,16,0])  -->  [16,16,0,0]
merge([16,16,0,0]) -->  [32,0,0,0]
```
"""

def merge_tiles(line):
    """
    Merges identical tiles in a single row according to the rules of the 2048 game.

    Parameters:
    line (list of int): A list of integers representing the tile values in a single row.

    Returns:
    list of int: A new list with the tile values from line slid towards the front of the array (index 0) and merged.
    """
    from itertools import groupby

    merged = []
    for (k, g) in groupby((v for v in line if v)):
        g = list(g)
        (n, r) = divmod(len(g), 2)
        if n:
            merged.extend([k * 2] * n)
        if r:
            merged.append(k)
    return merged + [0] * (len(line) - len(merged))