"""
QUESTION:
Implement a function `find_path` that takes a 2D array, a source point, and a destination point as input. The function should find a path from the source point to the destination point in the 2D array while avoiding obstacles represented by a value of 1. The function should return the path as a list of coordinates if it exists, otherwise it should return `None`. 

The source and destination points are valid if they are within the bounds of the 2D array. The function can move in all four directions (up, down, left, right) but cannot move through obstacles. If there are multiple paths, any valid path can be returned.
"""

def find_path(array, source, destination):
    rows = len(array)
    cols = len(array[0])
    
    # Check if source and destination are valid
    if source[0] < 0 or source[0] >= rows or source[1] < 0 or source[1] >= cols:
        return None
    if destination[0] < 0 or destination[0] >= rows or destination[1] < 0 or destination[1] >= cols:
        return None
    
    # Create a visited array to keep track of visited cells
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    # Create a path array to store the path
    path = []
    
    # Call the recursive helper function to find the path
    if find_path_helper(array, source, destination, visited, path):
        return path
    else:
        return None

def find_path_helper(array, current, destination, visited, path):
    # Check if current cell is the destination
    if current == destination:
        path.append(current)
        return True
    
    rows = len(array)
    cols = len(array[0])
    
    x, y = current
    
    # Check if current cell is a valid cell
    if x < 0 or x >= rows or y < 0 or y >= cols or array[x][y] == 1 or visited[x][y]:
        return False
    
    # Mark current cell as visited
    visited[x][y] = True
    
    # Add current cell to the path
    path.append(current)
    
    # Recursive call to find path in all four directions
    if find_path_helper(array, [x-1, y], destination, visited, path) or \
       find_path_helper(array, [x+1, y], destination, visited, path) or \
       find_path_helper(array, [x, y-1], destination, visited, path) or \
       find_path_helper(array, [x, y+1], destination, visited, path):
        return True
    
    # If no path found, backtrack and remove current cell from the path
    path.pop()
    
    return False