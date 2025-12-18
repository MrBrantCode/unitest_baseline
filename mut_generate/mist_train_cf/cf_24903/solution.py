"""
QUESTION:
Design a function called `navigate_maze` that uses a Depth-First Search approach to find a path from the start to the end of a given maze. The maze is represented as a grid where 0 indicates an open path and 1 indicates a wall. The start and end points of the maze are given.
"""

def navigate_maze(maze, start, end):
    """
    This function navigates through a given maze from a start point to an end point.
    
    Args:
    maze (list): A 2D list representing the maze. 0 indicates an open path and 1 indicates a wall.
    start (tuple): The coordinates of the start point in the maze.
    end (tuple): The coordinates of the end point in the maze.
    
    Returns:
    list: A list of coordinates representing the path from the start to the end of the maze. If no path exists, returns None.
    """

    # Define the possible directions in the maze (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Create a visited set to keep track of visited cells
    visited = set()
    
    # Define a helper function to perform the depth-first search
    def dfs(current, path):
        # If the current cell is the end, return the path
        if current == end:
            return path
        
        # Mark the current cell as visited
        visited.add(current)
        
        # Explore all neighbors of the current cell
        for direction in directions:
            x, y = current[0] + direction[0], current[1] + direction[1]
            
            # Check if the neighbor is within the maze boundaries and is not a wall and not visited
            if (0 <= x < len(maze)) and (0 <= y < len(maze[0])) and maze[x][y] == 0 and (x, y) not in visited:
                # Recursively call the dfs function on the neighbor
                result = dfs((x, y), path + [(x, y)])
                
                # If a path is found, return it
                if result:
                    return result
        
        # If no path is found, return None
        return None
    
    # Call the dfs function on the start point
    return dfs(start, [start])