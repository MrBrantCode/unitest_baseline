"""
QUESTION:
Perform an "advanced flood fill" on a given 2D image array. The function, `advancedFloodFill`, takes in a 2D image array `image`, the starting row `sr`, the starting column `sc`, the new color `newColor`, and a threshold value `threshold`. The function should replace the color of the starting pixel and any connected pixels (4-directionally) with the same color as the starting pixel (within the given threshold) with the new color. The function should return the modified image. The length of `image` and `image[0]` will be in the range `[1, 50]` and `0 <= sr < image.length` and `0 <= sc < image[0].length`. The value of each color in `image[i][j]`, `newColor`, and `threshold` will be an integer in `[0, 65535]`.
"""

def advancedFloodFill(image, sr, sc, newColor, threshold):
    rows, cols = len(image), len(image[0])
    color = image[sr][sc]
    visited = [[0]*cols for _ in range(rows)]
    
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or visited[r][c] or abs(image[r][c] - color) > threshold:
            return
        visited[r][c] = 1
        image[r][c] = newColor
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)
        
    dfs(sr, sc)
    return image