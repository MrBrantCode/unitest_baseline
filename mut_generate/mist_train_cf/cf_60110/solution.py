"""
QUESTION:
Write a function `openLock(deadends, obstacles, target)` that takes in three parameters: 
- `deadends`: a list of strings, each representing a combination that will stop the lock's wheels from turning
- `obstacles`: a list of strings, each representing a combination that will require an extra move to continue
- `target`: a string representing the combination to unlock the lock

The function should return the minimum number of turns required to open the lock, or -1 if it's impossible. Each turn can increment or decrement a wheel by one slot. The wheels wrap around, and the lock starts at '00000'.
"""

from collections import deque
def openLock(deadends, obstacles, target):
    visited, dead, obstacle  = set('00000'), {x: 1 for x in deadends}, {x: 1 for x in obstacles}
    q = deque([('00000', 0)])
    
    while q:
        node, depth = q.popleft()
        if node == target: return depth
        if node in dead: continue
        
        for i in range(4):
            for dir in [-1, 1]:
                n = node[:i] + str((int(node[i]) + dir) % 10) + node[i + 1:]
                if n not in visited:
                    visited.add(n)
                    q.append((n, depth + 1 + (n in obstacle)))
    return -1