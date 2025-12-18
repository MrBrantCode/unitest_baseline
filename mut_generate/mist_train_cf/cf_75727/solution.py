"""
QUESTION:
Create a function `gardenNoAdj` that takes two parameters: an integer `n` representing the number of gardens and a 2D list `paths` where each sublist contains two integers representing a bidirectional path between two gardens. The function should return a list where the `i-th` element represents the type of flower to be planted in the `(i+1)th` garden. Each garden can only plant one of 4 types of flowers, and for any two gardens connected by a path, they must have different types of flowers. Additionally, no three gardens connected in a triangle can have the same sequence of flower types, and no two gardens that are not directly connected can have the same type of flower. The total number of each type of flower across all gardens should be as equal as possible. It is guaranteed that an answer exists.
"""

def gardenNoAdj(n, paths):
    G = [[] for i in range(n)]
    for x, y in paths:
        G[x-1].append(y-1)
        G[y-1].append(x-1)
    flowers = [0] * n
    for i in range(n):
        colors = set(range(1, 5))
        colors -= set(flowers[j] for j in G[i])
        flowers[i] = colors.pop()
    return flowers