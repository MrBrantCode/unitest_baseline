"""
QUESTION:
Design a function `minimumJumps(forbidden, a, b, x)` that determines the least number of jumps a bug needs to reach its home at position `x`, given an array of forbidden positions `forbidden`, and the bug's movement rules: it can leap forward exactly `a` positions or jump backward `b` positions. The bug cannot jump backward consecutively and must avoid any forbidden positions. If no feasible sequence of jumps allows the bug to land on position `x`, return `-1`.

The function has the following constraints:
- `1 <= len(forbidden) <= 1000`
- `1 <= a, b, forbidden[i] <= 2000`
- `0 <= x <= 2000`
- All elements in `forbidden` are unique.
- Position `x` is not forbidden.
"""

from collections import deque

def minimumJumps(forbidden, a, b, x):
    """
    This function determines the least number of jumps a bug needs to reach its home at position `x`, 
    given an array of forbidden positions `forbidden`, and the bug's movement rules: it can leap forward 
    exactly `a` positions or jump backward `b` positions.

    Args:
    forbidden (list): A list of forbidden positions.
    a (int): The forward jump size.
    b (int): The backward jump size.
    x (int): The target position.

    Returns:
    int: The minimum number of jumps to reach the target position. Returns -1 if no feasible sequence exists.
    """

    maxPos = 2000 + max(forbidden) + a + b
    visited = set()
    blocked = set(forbidden)
    
    q = deque([(0, 0)])
    visited.add((0, 0))
    
    while q:
        d, pos = q.popleft()
        if pos == x:
            return d
        if pos + a < maxPos and (pos + a, 1) not in visited and pos + a not in blocked:
            visited.add((pos + a, 1))
            q.append((d + 1, pos + a))
        if pos - b >= 0 and (pos - b, 0) not in visited and pos - b not in blocked:
            visited.add((pos - b, 0))
            q.append((d + 1, pos - b))
    return -1