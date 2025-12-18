"""
QUESTION:
Given an array of non-negative integers `arr`, a start index `start`, and a target value `target`, determine if it's possible to reach an index with the value equal to `target` by jumping to `i + arr[i]` or `i - arr[i]` from the current index `i`, without jumping outside the array. The function should be named `canReach` and take `arr`, `start`, and `target` as inputs. The constraints are `1 <= arr.length <= 5 * 10^4`, `0 <= arr[i] < arr.length`, `0 <= start < arr.length`, and `0 <= target < arr.length`.
"""

from collections import defaultdict,deque

def canReach(arr, start, target):
    n = len(arr)
    visited = [0] * n
    graph = defaultdict(list)
    
    # Create a graph of possible jumps
    for i in range(n):
        if i + arr[i] < n:
            graph[i].append(i + arr[i])
        if i - arr[i] >= 0:
            graph[i].append(i - arr[i])

    # Breadth-first search
    q = deque([start])
    visited[start] = 1
    while q:
        node = q.popleft()
        if arr[node] == target:
            return True
        for nei in graph[node]:
            if not visited[nei]:
                q.append(nei)
                visited[nei] = 1
    return False