"""
QUESTION:
You have a grid with `$m$` rows and `$n$` columns. Return the number of unique ways that start from the top-left corner and go to the bottom-right corner. You are only allowed to move right and down.

For example, in the below grid of `$2$` rows and `$3$` columns, there are `$10$` unique paths:

```
o----o----o----o
|    |    |    |
o----o----o----o
|    |    |    |
o----o----o----o
```

**Note:** there are random tests for grids up to 1000 x 1000 in most languages, so a naive solution will not work.

---
*Hint: use mathematical permutation and combination*
"""

from math import factorial

def unique_paths(m: int, n: int) -> int:
    """
    Calculate the number of unique paths from the top-left corner to the bottom-right corner
    in a grid with `m` rows and `n` columns, where only right and down movements are allowed.

    Parameters:
    - m (int): Number of rows in the grid.
    - n (int): Number of columns in the grid.

    Returns:
    - int: The number of unique paths.
    """
    return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))