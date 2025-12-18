"""
QUESTION:
Given a positive integer K, find the length of the smallest positive integer N such that N is divisible by K, and N only contains the digit 1 or 0. Return the length of N. If there is no such N, return -1. Additionally, return the number of 1s and 0s in N. The input constraint is 1 <= K <= 10^5.
"""

from collections import deque, namedtuple

Node = namedtuple('Node', 'val, length, ones, zeros')

def smallestRepunitDivByK(K):
    if K % 2 == 0 or K % 5 == 0:
        return -1, -1, -1

    visited = set()
    queue = deque()
    queue.append(Node(1, 1, 1, 0))

    while queue:
        node = queue.popleft()
        mod = node.val % K
        if mod == 0:
            return node.length, node.ones, node.zeros
        if mod not in visited:
            visited.add(mod)
            queue.append(Node((mod*10)%K, node.length+1, node.ones, node.zeros+1))
            queue.append(Node((mod*10+1)%K, node.length+1, node.ones+1, node.zeros))

    return -1, -1, -1