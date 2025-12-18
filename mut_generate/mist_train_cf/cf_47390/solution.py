"""
QUESTION:
Design a function `min_operations` that calculates the minimum number of operations (addition and subtraction of 1) required to reach a given `target` number from a given `start` number. The function should take two parameters: `start` and `target`, and return the minimum number of operations.
"""

from collections import deque

def min_operations(start, target):
    queue = deque([(start, 0)])
    visited = {start}
    
    while queue:
        current, step = queue.popleft()
        
        if current == target:
            return step
        
        if current - 1 not in visited:
            visited.add(current - 1)
            queue.append((current - 1, step + 1))
        
        if current + 1 not in visited:
            visited.add(current + 1)
            queue.append((current + 1, step + 1))