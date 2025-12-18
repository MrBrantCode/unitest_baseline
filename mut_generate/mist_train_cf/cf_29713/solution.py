"""
QUESTION:
Write a function `largestBlackRegionBoundingBox` that takes a 2D binary grid `image` as input, where 1s represent black pixels and 0s represent white pixels. The function should return the coordinates of the bounding box of the largest black region in the image, represented by the coordinates of its top-left and bottom-right corners. The function should return `Tuple[Tuple[int, int], Tuple[int, int]]` and the coordinates should be 0-indexed. The function should not modify the input image and should handle the case where the input image is empty.
"""

from typing import List, Tuple

def largestBlackRegionBoundingBox(image: List[List[int]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    def dfs(row, col, visited):
        if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]) or image[row][col] == 0 or visited[row][col]:
            return 0
        visited[row][col] = True
        return 1 + dfs(row+1, col, visited) + dfs(row-1, col, visited) + dfs(row, col+1, visited) + dfs(row, col-1, visited)

    max_area = 0
    top_left = (0, 0)
    bottom_right = (0, 0)
    visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == 1 and not visited[i][j]:
                area = dfs(i, j, visited)
                if area > max_area:
                    max_area = area
                    min_row = i
                    min_col = j
                    max_row = i
                    max_col = j
                    for x in range(len(image)):
                        for y in range(len(image[0])):
                            if visited[x][y]:
                                min_row = min(min_row, x)
                                max_row = max(max_row, x)
                                min_col = min(min_col, y)
                                max_col = max(max_col, y)
                    top_left = (min_row, min_col)
                    bottom_right = (max_row, max_col)
    return top_left, bottom_right