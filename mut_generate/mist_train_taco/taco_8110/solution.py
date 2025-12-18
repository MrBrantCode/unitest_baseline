"""
QUESTION:
There are some candies that need to be distributed to some children as fairly as possible (i.e. the variance of result needs to be as small as possible), but I don't know how to distribute them, so I need your help. Your assignment is to write a function with signature `distribute(m, n)` in which `m` represents how many candies there are, while `n` represents how many children there are. The function should return a container which includes the number of candies each child gains.

# Notice
1. *The candy can't be divided into pieces.*
2. The list's order doesn't matter.

# Requirements
1. The case `m < 0` is equivalent to `m == 0`.
2. If `n <= 0` the function should return an empty container. 
3. If there isn't enough candy to distribute, you should fill the corresponding number with `0`.

# Examples
```python
distribute(-5,  0) # should be [] 
distribute( 0,  0) # should be [] 
distribute( 5,  0) # should be [] 
distribute(10,  0) # should be [] 
distribute(15,  0) # should be [] 
distribute(-5, -5) # should be [] 
distribute( 0, -5) # should be [] 
distribute( 5, -5) # should be [] 
distribute(10, -5) # should be [] 
distribute(15, -5) # should be []
distribute(-5, 10) # should be [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
distribute( 0, 10) # should be [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
distribute( 5, 10) # should be [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
distribute(10, 10) # should be [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
distribute(15, 10) # should be [2, 2, 2, 2, 2, 1, 1, 1, 1, 1]
```
  
# Input
  1. m: Integer (m <= 100000)
  2. n: Integer (n <= 1000)

# Output
  1. [Integer]
"""

def distribute_candies(m: int, n: int) -> list[int]:
    """
    Distributes `m` candies to `n` children as fairly as possible.

    Parameters:
    - m (int): The number of candies to distribute. If m < 0, it is treated as 0.
    - n (int): The number of children to distribute candies to. If n <= 0, the function returns an empty list.

    Returns:
    - list[int]: A list where each element represents the number of candies each child receives.
    """
    if n <= 0:
        return []
    
    m = max(m, 0)  # Treat negative m as 0
    q, r = divmod(m, n)
    
    # Each child gets at least q candies, and the first r children get an extra candy
    return [q + (1 if i < r else 0) for i in range(n)]