"""
QUESTION:
Vasya wants to climb up a stair of certain amount of steps (Input parameter 1). There are 2 simple rules that he has to stick to.

1. Vasya can climb 1 or 2 steps at each move.
2. Vasya wants the number of moves to be a multiple of a certain integer. (Input parameter 2).

### Task:
What is the `MINIMAL` number of moves making him climb to the top of the stairs that satisfies his conditions?

### Input

1. Number of stairs:    `0 <  N  ≤ 10000` ;
2. Integer to be multiplied : `1 < M ≤ 10 `;

### Output

1. Return a single integer - the minimal number of moves being a multiple of M;
2. If there is no way he can climb satisfying condition return - 1 instead. (`Nothing` in Haskell)

### Examples

```python
numberOfSteps(10, 2) => 6  # Sequence of steps : {2, 2, 2, 2, 1, 1}

numberOfSteps(3, 5) => -1 # !Possible sequences of steps : {2, 1}, {1, 2}, {1, 1, 1}
```
``` haskell
numberOfSteps 10 2 == Just 6  -- Sequence of steps : {2, 2, 2, 2, 1, 1}
numberOfSteps  3 5 == Nothing -- Not possible, since the sequences of steps would be {2, 1}, {1, 2} or {1, 1, 1}
```
"""

def minimal_moves(steps: int, m: int) -> int:
    if steps < m:
        return -1
    
    # Calculate the minimum number of moves required to reach the top
    min_moves = (steps + 1) // 2  # This is the ceiling of steps / 2
    
    # Check if the minimum number of moves is already a multiple of m
    if min_moves % m == 0:
        return min_moves
    
    # Otherwise, find the next multiple of m
    next_multiple = ((min_moves // m) + 1) * m
    
    # Check if the next multiple is within the possible range of moves
    if next_multiple <= steps:
        return next_multiple
    
    return -1