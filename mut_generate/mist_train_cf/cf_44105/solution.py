"""
QUESTION:
Determine the sum of P(2^p^5 - 1, 2^q^5 - 1) modulo 1,000,000,007 for all combinations of prime numbers p and q, where p < q < 1000. The function P(a, b) represents the least number of pourings required to measure one liter, given the capacities of the buckets S, M, L are a, b, and a + b liters respectively, with a and b being coprime positive integers and a <= b.
"""

from collections import deque

def entrance(a, b):
    """
    Calculate the least number of pourings required to measure one liter.

    Args:
        a (int): The capacity of bucket S in liters.
        b (int): The capacity of bucket M in liters.

    Returns:
        int: The least number of pourings required to measure one liter.
    """
    if a == 1 or b == 1:
        return 0
    max_value = a + b
    graph = [[] for _ in range(max_value + 1)]
    for i in range(1, max_value + 1):
        for j in range(1, max_value + 1):
            if i != j:
                graph[i].append((j, 1))
                graph[j].append((i, 1))
        if i * 2 <= max_value:
            graph[i].append((i * 2, 0))
    d = [float('inf')] * (max_value + 1)
    d[a] = 0
    queue = deque([a])
    while queue:
        u = queue.popleft()
        for v, w in graph[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                queue.append(v)
    return d[1]