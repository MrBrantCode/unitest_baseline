"""
QUESTION:
Write a function `minPath` that takes as input a 2D grid of distinct integers and an integer `k`, and returns the shortest sequence of `k` elements that can be formed by starting from any cell in the grid and moving to neighboring cells (up, down, left, or right). The function should be able to handle erroneous input or data without producing an error. The grid should be an NxN matrix where N is 2 or greater, and the elements in the matrix are distinct integers from 1 through N^2.
"""

from typing import List
import heapq
from collections import deque

def getNeighbors(i: int, j: int, n: int) -> List[List[int]]:
    # Get all valid neighbours in grid for a cell at (i,j)
    neighbors = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    return [[x+i, y+j] for x, y in neighbors if 0 <= x+i < n and 0 <= y+j < n]

def minPath(grid: List[List[int]], k: int) -> List[int]:
    # Checking for erroneous input
    if not isinstance(grid, list) or not all(isinstance(i, list) for i in grid):
        return "Invalid input. Input has to be a 2D grid."
    n = len(grid)
    if not isinstance(k, int) or not 1 <= k <= n*n:
        return "Invalid input. k has to be an integer and within range."
    if any(not isinstance(i, int) for sublist in grid for i in sublist):
        return "Invalid input. Grid should only contain integers."

    heap = [[grid[0][0], [0, 0]]]   # value at cell, coords
    sumCache = {(0, 0): grid[0][0]}   # Cache total path sum at each cell. Key is coords
    pathCache = {(0, 0): [grid[0][0]]}   # Cache path at each cell. Key is coords

    while heap:
        curvalue, (curi, curj) = heapq.heappop(heap)
        # Generate all paths from current cell to neighbours
        for nexti, nextj in getNeighbors(curi, curj, n):
            newSum = sumCache[(curi, curj)] + grid[nexti][nextj]
            newPath = pathCache[(curi, curj)] + [grid[nexti][nextj]]
            if len(newPath) > k:   # If path too long, skip
                continue
            # If cell not visited yet or new path is shorter than existing, update cell's path sum
            if (nexti, nextj) not in sumCache or newSum < sumCache[(nexti, nextj)]:
                sumCache[(nexti, nextj)] = newSum
                heapq.heappush(heap, [newSum, [nexti, nextj]])
                pathCache[(nexti, nextj)] = newPath
    # Return min path among all the paths of len k
    return min((path for path in pathCache.values() if len(path)==k), key=sum)