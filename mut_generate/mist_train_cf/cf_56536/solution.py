"""
QUESTION:
Write a function `walls_no_gates` that takes a 2D list `rooms` as input, where each element in the list represents a room. The elements in the list can be either an integer or 2147483646, where 0 represents a gate, negative numbers represent walls, and 2147483646 represents an empty room. The function should start a depth-first search from every gate and every empty room, and update the distance of each room from the gate.

Restrictions: You can only use a depth-first search (dfs) to solve this problem, and the function `walls_no_gates` should not return anything.
"""

def walls_no_gates(rooms):
    if not rooms:
        return
    m, n = len(rooms), len(rooms[0])
    def dfs(i, j, d):
        if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]) or rooms[i][j] < d:
            return
        rooms[i][j] = d
        dfs(i-1, j, d + 1)
        dfs(i+1, j, d + 1)
        dfs(i, j-1, d + 1)
        dfs(i, j+1, d + 1)

    for i in range(m):
        for j in range(n):
            if rooms[i][j] in (0, 2147483646):
                dfs(i, j, 0)