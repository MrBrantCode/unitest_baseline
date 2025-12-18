"""
QUESTION:
Write a function `update_grid(grid, segments)` that updates the grid based on the line segments and returns the updated grid. The function takes a 2D array `grid` with all cells initialized to 0 and a list of line segments `segments`, where each segment is represented as a list of four integers [x1, y1, x2, y2], as input. The grid is based on a coordinate system where the x-axis represents columns and the y-axis represents rows. A cell is considered to be touched by a line segment if the line segment passes through or covers the cell.
"""

def update_grid(grid, segments):
    for segment in segments:
        x1, y1, x2, y2 = segment
        if x1 == x2:  
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[y][x1] += 1
        elif y1 == y2:  
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1][x] += 1
    return grid