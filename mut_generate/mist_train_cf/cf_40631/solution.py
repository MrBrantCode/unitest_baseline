"""
QUESTION:
You are given a list of triplets, where each triplet contains two individual IDs and a binary connection status. Write a function `countConnectedComponents` that takes this list as input and returns the number of connected components. The input list `triplets` consists of lists `[a, b, c]`, where `a` and `b` are positive integers representing individual IDs and `c` is either 0 or 1 indicating the connection status. The function should handle a list of any length and return the total number of connected components.
"""

from typing import List

def countConnectedComponents(triplets: List[List[int]]) -> int:
    individuals = set()
    for triplet in triplets:
        individuals.add(triplet[0])
        individuals.add(triplet[1])

    n = len(individuals)
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    for triplet in triplets:
        if triplet[2] == 1:
            union(triplet[0] - 1, triplet[1] - 1)

    components = set()
    for i in range(n):
        components.add(find(i))

    return len(components)