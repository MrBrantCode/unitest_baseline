"""
QUESTION:
Write a function `min_operations(X, Y)` that takes two integers `X` and `Y` as input, where `X` is the initial number on a broken calculator and `Y` is the target number, and returns the minimum number of operations needed to display `Y` from `X` using the operations "Double", "Decrement", and "Square". The calculator's display can only show numbers between 1 and 10^9. Assume `Y` is always a perfect square.
"""

from collections import deque

def min_operations(X: int, Y: int) -> int:
    queue = deque([(X, 0)])
    visited = {X}
    while queue:
        num, step = queue.popleft()
        if num == Y:
            return step
        for next_num in [num * 2, num - 1, num * num]:
            if next_num not in visited and 1 <= next_num <= Y:
                visited.add(next_num)
                queue.append((next_num, step + 1))
    return -1