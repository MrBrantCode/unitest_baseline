"""
QUESTION:
Implement a function `floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]` that takes a 2D grid of integers `image`, the row `sr` and column `sc` of a starting pixel, and a new color `newColor`. The function should return the updated image after filling all pixels connected to the starting pixel with the new color using depth-first search. The starting pixel's color is different from the new color.
"""

from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    rows, cols = len(image), len(image[0])
    currColor = image[sr][sc]

    def dfs(x: int, y: int):
        if x < 0 or x >= rows or y < 0 or y >= cols or image[x][y] != currColor or image[x][y] == newColor:
            return
        image[x][y] = newColor
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

    dfs(sr, sc)
    return image