"""
QUESTION:
Given three jugs with capacities `jug1Capacity`, `jug2Capacity`, and `jug3Capacity` liters and an infinite amount of water supply, determine whether it is possible to measure exactly `targetCapacity` liters using these three jugs. If measurable, return `True` and the minimum number of operations (fill, empty, or pour) to achieve the `targetCapacity`. Otherwise, return `False` and 0. 

Restrictions: `1 <= jug1Capacity, jug2Capacity, jug3Capacity, targetCapacity <= 10^6`.
"""

from collections import deque

def waterjugproblem(jug1Capacity, jug2Capacity, jug3Capacity, targetCapacity):
    if targetCapacity > jug1Capacity + jug2Capacity + jug3Capacity:
        return False, 0

    queue = deque([(0, 0, 0)])
    visited = set((0, 0, 0))
    min_operations = 0

    while queue:
        size = len(queue)
        while size > 0:
            a, b, c = queue.popleft()
            if a == targetCapacity or b == targetCapacity or c == targetCapacity:
                return True, min_operations
            for x, y, z in [(a, b, min(jug3Capacity, a+b+c)), (a, min(jug2Capacity, a+b+c), c), (min(jug1Capacity, a+b+c), b, c), 
                            (a, b, 0), (a, 0, c), (0, b, c), 
                            (a, min(b+c, jug2Capacity), max(0, b+c-jug2Capacity)), (min(a+c, jug1Capacity), b, max(0, a+c-jug1Capacity)), (max(0, a+b-jug1Capacity), min(a+b, jug2Capacity), c)]:
                if (x, y, z) not in visited:
                    visited.add((x, y, z))
                    queue.append((x, y, z))
            size -= 1
        min_operations += 1

    return False, 0