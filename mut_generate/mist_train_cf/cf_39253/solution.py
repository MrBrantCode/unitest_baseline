"""
QUESTION:
Implement a method `solve` that takes two positive integers `N` and `S` as input and returns a 2D array of size (N+1) x (S+1) filled according to the following rules: 

- Initialize the array with zeros and set `arr[0][0]` to 1.
- For each index (n, s) where n ranges from 0 to N-1 and s ranges from 0 to S-1, update `arr[n+1][s+1]` to be the same as `arr[n][s]`.

Return the modified array. 

Function signature: `def solve(self, N: int, S: int) -> List[List[int]]`
"""

from typing import List

def solve(N: int, S: int) -> List[List[int]]:
    arr = [[0] * (S + 1) for _ in range(N + 1)]
    arr[0][0] = 1
    for n in range(N):
        for s in range(S):
            if arr[n][s] == 1:
                arr[n+1][s+1] = 1
            else:
                arr[n+1][s+1] = 0
    return arr