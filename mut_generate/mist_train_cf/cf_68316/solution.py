"""
QUESTION:
Write a function `num_trees(n)` to calculate and return the number of structurally distinct binary search trees (BST's) that contain exactly `n` nodes, where each node has a unique value from `1` to `n`. The input `n` is an integer and should be between `1` and `19` (inclusive).
"""

def num_trees(n):
    G = [0] * (n + 1)
    G[0] = 1
    G[1] = 1

    for i in range(2, n+1):
        for j in range(1, i+1):
            G[i] += G[j-1] * G[i-j]

    return G[n]