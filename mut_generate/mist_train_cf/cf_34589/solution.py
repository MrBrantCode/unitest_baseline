"""
QUESTION:
You are given a grid representing an asteroid field with '#' representing an asteroid and '.' representing an empty space. Write a function `find_best_observation_point(grid: List[str])` to find the location (x, y) of the best observation point from which the maximum number of asteroids can be observed without any obstructions in the same row, column, or diagonal. The grid will have at least one asteroid and will be non-empty and rectangular.
"""

from typing import List, Tuple

def find_best_observation_point(grid: List[str]) -> Tuple[int, int]:
    max_observed = 0
    best_point = (0, 0)
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.':
                observed = sum(grid[i][k] == '#' for k in range(cols))  
                observed += sum(grid[k][j] == '#' for k in range(rows))  

                k, l = i, j
                while k < rows and l < cols:
                    observed += grid[k][l] == '#'
                    k += 1
                    l += 1

                k, l = i, j
                while k < rows and l >= 0:
                    observed += grid[k][l] == '#'
                    k += 1
                    l -= 1

                if observed > max_observed:
                    max_observed = observed
                    best_point = (j, i)  

    return best_point