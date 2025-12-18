"""
QUESTION:
Given a string `path` representing movements ('N', 'S', 'E', 'W') and a list of tuples `obstacles` representing coordinates, write a function `isPathCrossing` that returns `True` if the path crosses itself or hits an obstacle, and `False` otherwise. The function should consider the constraints that `1 <= path.length <= 10^4` and `0 <= obstacles.length <= 10^4`.
"""

def isPathCrossing(path, obstacles):
  x, y = 0, 0
  visited = {(0, 0)} # Starting point
  
  # Add obstacles to set
  for ox, oy in obstacles:
    visited.add((ox, oy))
  
  # Direction vectors
  dx = {"N": 0, "S": 0, "E": 1, "W": -1}
  dy = {"N": 1, "S": -1, "E": 0, "W": 0}
  
  for direction in path:
    x += dx[direction]
    y += dy[direction]
    if (x, y) in visited: # Check if new location has been visited or is an obstacle
      return True
      
    visited.add((x, y))
  
  return False