"""
QUESTION:
Write a function `minOperations(jug1Capacity, jug2Capacity, jug3Capacity, targetCapacity)` that takes the capacities of three jugs and a target capacity as input. The function should return a tuple of two values: a boolean indicating whether it's possible to measure the target capacity using the three jugs, and the minimum number of operations (filling, emptying, and pouring) required to measure the target capacity. If it's impossible to measure the target capacity, return `False, 0`.
"""

from collections import deque

def minOperations(jug1Capacity, jug2Capacity, jug3Capacity, targetCapacity):
    if targetCapacity > jug1Capacity + jug2Capacity + jug3Capacity:
        return False, 0

    queue = deque([[0, 0, 0]])
    visited = set([(0, 0, 0)])
    min_operations = 0

    while queue:
        size_ = len(queue)
        while size_ > 0:
            a, b, c = queue.popleft()
            if a == targetCapacity or b == targetCapacity or c == targetCapacity:
                return True, min_operations
            for x, y, z in [(a, b, min(jug3Capacity, a+b+c)), (a, min(jug2Capacity, a+b+c), c), (min(jug1Capacity, a+b+c), b, c), (a, b, 0), (a, 0, c), (0, b, c), (a, min(b+c, jug2Capacity), max(0, b+c-jug2Capacity)), (min(a+c, jug1Capacity), b, max(0, a+c-jug1Capacity)), (max(0, a+b-jug1Capacity), min(a+b, jug2Capacity), c)]:
                if (x, y, z) not in visited:
                    visited.add((x, y, z))
                    queue.append([x, y, z])
            size_ -= 1
        min_operations += 1

    return False, 0