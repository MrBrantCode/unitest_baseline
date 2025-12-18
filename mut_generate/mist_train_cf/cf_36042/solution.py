"""
QUESTION:
Write a function `shortestToChar(S, C)` that returns a list of integers representing the shortest distance from each character in the string `S` to the character `C`. For each character `S[i]` in the string `S`, the distance is calculated as the absolute difference between the indices of `S[i]` and the nearest occurrence of character `C`. 

Function signature: 
```python
def shortestToChar(S: str, C: str) -> List[int]:
```
The function should take a string `S` and a character `C` as input and return a list of integers. The length of the output list should be equal to the length of the input string `S`.
"""

from typing import List

def shortestToChar(S: str, C: str) -> List[int]:
    n = len(S)
    ret = [float('inf')] * n
    
    # Forward pass to calculate distances to the right
    prev = float('-inf')
    for i in range(n):
        if S[i] == C:
            prev = i
        ret[i] = min(ret[i], i - prev)

    # Backward pass to update distances to the left
    prev = float('inf')
    for i in range(n - 1, -1, -1):
        if S[i] == C:
            prev = i
        ret[i] = min(ret[i], prev - i)

    return ret