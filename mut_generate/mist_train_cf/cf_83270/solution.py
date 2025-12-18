"""
QUESTION:
Given a list of rooms where each room i contains a list of keys rooms[i] that unlock chambers numbered v, return true if and only if all chambers can be visited, starting from chamber 0.

The function to solve this problem is named canVisitAllRooms and it takes a 2D list rooms as input where 1 <= rooms.length <= 1000 and 0 <= rooms[i].length <= 1000. The total number of keys across all chambers does not exceed 3000.
"""

def canVisitAllRooms(rooms):
    visited = [False]*len(rooms)
    def dfs(node):
        visited[node] = True
        for key in rooms[node]:
            if not visited[key]:
                dfs(key)

    dfs(0)
    return all(visited)