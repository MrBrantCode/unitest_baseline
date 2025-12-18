"""
QUESTION:
Write a function named `min_median_route` that takes a 3D cube represented as a list of lists of lists where each cell is associated with a specific energy level, and returns the minimum median energy level of all existing routes from the top-left-front cell to the bottom-right-back cell, where a route can only move right, down, or deeper.
"""

def min_median_route(cube):
    """
    This function takes a 3D cube represented as a list of lists of lists where each cell is associated with a specific energy level,
    and returns the minimum median energy level of all existing routes from the top-left-front cell to the bottom-right-back cell.

    Args:
    cube (list of lists of lists): A 3D cube where each cell is associated with a specific energy level.

    Returns:
    int: The minimum median energy level of all existing routes from the top-left-front cell to the bottom-right-back cell.
    """
    # Get the dimensions of the cube
    m, n, p = len(cube), len(cube[0]), len(cube[0][0])

    # Define the directions for the DFS
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    def dfs(x, y, z, median):
        # Check if the current cell is out of bounds or its energy level is greater than the median
        if x < 0 or x >= m or y < 0 or y >= n or z < 0 or z >= p or cube[x][y][z] > median:
            return False
        # If the current cell is the destination, return True
        if x == m - 1 and y == n - 1 and z == p - 1:
            return True
        # Mark the current cell as visited
        temp, cube[x][y][z] = cube[x][y][z], float('inf')
        # Recursively check all possible directions
        for dx, dy, dz in directions:
            if dfs(x + dx, y + dy, z + dz, median):
                return True
        # Backtrack
        cube[x][y][z] = temp
        return False

    # Initialize the low and high values
    low, high = min(min(min(row) for row in plane) for plane in cube), max(max(max(row) for row in plane) for plane in cube)

    # Perform the binary search
    while low <= high:
        mid = (low + high) // 2
        if dfs(0, 0, 0, mid):
            high = mid - 1
        else:
            low = mid + 1

    return low