"""
QUESTION:
Implement a depth-first search (DFS) algorithm to find a path from the entrance to the exit in a given labyrinth, considering efficiency and data structure utilization. The labyrinth can be represented as a 2D array, and the entrance and exit are marked with specific coordinates. Your implementation should be non-recursive and use data structures such as a stack and a visited array to keep track of the path. The algorithm should be able to recover the shortest path from the entrance to the exit using a predecessor array and avoid infinite loops by checking visited nodes.
"""

def labyrinth_dfs(labyrinth, entrance, exit):
    """
    This function implements a depth-first search algorithm to find a path 
    from the entrance to the exit in a given labyrinth.

    Args:
    labyrinth (2D array): A 2D array representing the labyrinth.
    entrance (tuple): The coordinates of the entrance in the labyrinth.
    exit (tuple): The coordinates of the exit in the labyrinth.

    Returns:
    list: A list of coordinates representing the path from the entrance to the exit.
    """

    # Initialize a visited array to keep track of visited nodes
    visited = [[False for _ in range(len(labyrinth[0]))] for _ in range(len(labyrinth))]

    # Initialize a predecessor array to record the path
    predecessor = [[None for _ in range(len(labyrinth[0]))] for _ in range(len(labyrinth))]

    # Initialize a stack to store nodes to visit
    stack = [entrance]

    # Mark the entrance as visited
    visited[entrance[0]][entrance[1]] = True

    # Define the possible movements in the labyrinth (up, down, left, right)
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Perform the DFS
    while stack:
        x, y = stack.pop()

        # If the current node is the exit, construct the path
        if (x, y) == exit:
            path = []
            while (x, y) != entrance:
                path.append((x, y))
                x, y = predecessor[x][y]
            path.append(entrance)
            path.reverse()
            return path

        # Explore the neighbors of the current node
        for dx, dy in movements:
            nx, ny = x + dx, y + dy

            # Check if the neighbor is within the labyrinth boundaries and not visited
            if (0 <= nx < len(labyrinth) and 0 <= ny < len(labyrinth[0]) and 
                labyrinth[nx][ny] != 1 and not visited[nx][ny]):
                stack.append((nx, ny))
                visited[nx][ny] = True
                predecessor[nx][ny] = (x, y)

    # If there is no path to the exit, return None
    return None