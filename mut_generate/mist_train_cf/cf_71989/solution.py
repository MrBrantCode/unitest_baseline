"""
QUESTION:
Write a function `min_swaps_binary(source, target)` that takes two binary strings `source` and `target` of the same length and returns a tuple containing the minimum number of swaps required to convert `source` to `target` and a list of tuples representing the sequence of swaps performed, where each tuple contains the indices of the two bits that were swapped.
"""

from collections import deque

def min_swaps_binary(source, target):
    if source == target:
        return (0, [])
    
    N = len(source)
    queue = deque([(source, 0, [])])
    visited = {source: 0}
    
    while queue:
        curr, dist, swaps = queue.popleft()
        
        for i in range(N):
            for j in range(i+1, N):
                if curr[i] != curr[j]:
                    swapped = curr[:i] + curr[j] + curr[i+1:j] + curr[i] + curr[j+1:]
                    if swapped not in visited:
                        if swapped == target:
                            swaps.append((i, j))
                            return (dist + 1, swaps)
                        queue.append((swapped, dist + 1, swaps + [(i, j)]))
                        visited[swapped] = dist + 1
    return (-1, [])