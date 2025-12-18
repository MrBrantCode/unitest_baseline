"""
QUESTION:
Write a function `escapeGhosts(ghosts, target)` that takes two parameters: `ghosts` (a list of ghost positions) and `target` (the destination point). The function should return `True` if it's possible to escape the ghosts and reach the target, and `False` otherwise. 

The starting point is assumed to be `[0, 0]`. All coordinates are integral and can be between -10^4 and 10^4. Multiple ghosts can occupy the same location. The length of `ghosts` is between 1 and 100, and each ghost's position is a list of two integers. The `target` is a list of two integers.
"""

def escapeGhosts(ghosts, target):
    dist = abs(target[0]) + abs(target[1])
    return all(dist < abs(target[0] - ghost[0]) + abs(target[1] - ghost[1]) for ghost in ghosts)