"""
QUESTION:
Implement a function `spiral_value(a, target_x, target_y)` that calculates the value at a specific coordinate `(target_x, target_y)` in a spiral pattern. The spiral pattern is generated based on a set of predefined coordinates and a while loop that continues until the value at the current position is greater than the given threshold value `a`. The function should return the value at the specified coordinates in the spiral pattern.
"""

def entance(a, target_x, target_y):
    coords = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    x, y = (0, 0)
    dx, dy = (1, 0)
    M = {(x, y): 1}

    while M[(x, y)] < a:
        x, y = x + dx, y + dy
        M[(x, y)] = sum([M[(x + ox, y + oy)] for ox, oy in coords if (x + ox, y + oy) in M])
        if (x == y) or (x > 0 and x == 1 - y) or (x < 0 and x == -y):
            dx, dy = -dy, dx

    return M.get((target_x, target_y), 0)