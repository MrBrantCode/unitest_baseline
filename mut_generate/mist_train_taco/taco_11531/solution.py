"""
QUESTION:
Laura Bassi was the first female professor at a European university.  
Despite her immense intellect, she was not always allowed to lecture publicly.

One day a professor with very strong beliefs against women in academia sent some `agents` to find Bassi and end her career.

Help her escape by telling her the safest places in town!

Task

```if:python,javascript
Implement the function `advice(agents, n)` where
```
```if:haskell
Implement the function `advice agents n :: [(Int,Int)] -> Int -> [(Int,Int)]` where
```
```if:swift
Implement the function `advice(agents: [[Int]], n: Int) -> [[Int]]` where
```

- `agents` is an array of agent coordinates.
- `n` defines the size of the city that Bassi needs to hide in, in other words the side length of the square grid. 

The function should return a list of coordinates that are the furthest away (by Manhattan distance) from all agents.

As an example, say you have a 6x6 map, and agents at locations

```python
[(0, 0), (1, 5), (5, 1)]
```

The distances to the nearest agent look like this.



The safest spaces are the ones with distance `4`, marked in bright red. So the function should return

```python
[(2, 2), (3, 3), (4, 4), (5, 5)]
```

in any order.

Edge cases:
- If there is an agent on every grid cell, there is no safe space, so return an empty list.
- If there are no agents, then every cell is a safe spaces, so return all coordinates.
- if `n` is `0`, return an empty list.
- If agent coordinates are outside of the map, they are simply not considered.
- There are no duplicate agents on the same square.

Performance

All reference solutions run in around 6 seconds.
You might not pass the tests if you use a brute-force solution.

```if-not:swift,javascript
There are `200` random tests with `n <= 50`. Inefficient solutions might time out.
```
```if:javascript
There are `300` random tests with `n <= 70`. Inefficient solutions might time out.
```
```if:swift
There are `200` random tests with `n <= 70`. Inefficient solutions might time out.
```

This kata is inspired by ThoughtWorks' coding challenge
"""

def find_safest_places(agents, n):
    # Initialize the frontier with valid agent positions
    frontier = {(x, y) for (x, y) in agents if 0 <= x < n and 0 <= y < n}
    
    # Initialize the bag with all possible positions in the grid
    bag = {(x, y) for x in range(n) for y in range(n)}
    
    # If all positions are occupied by agents, return an empty list
    if frontier == bag:
        return []
    
    # BFS-like approach to find the furthest positions from agents
    while frontier and bag > frontier:
        bag -= frontier
        frontier = {pos for (x, y) in frontier 
                    for pos in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)) 
                    if pos in bag}
    
    # Return the sorted list of safest places
    return sorted(bag)