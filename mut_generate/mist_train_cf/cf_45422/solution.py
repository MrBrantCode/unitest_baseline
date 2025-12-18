"""
QUESTION:
Write a function called `maximumInvitations(grid, preferences)` that finds the maximum number of invitations that can be accepted given a grid representing the availability of each person and a list of preferences for each person. The grid is a 2D list where `grid[i][j]` is 1 if person `i` is available for person `j` and 0 otherwise. The preferences is a 2D list where `preferences[i]` is a list of the people person `i` prefers in order. The function should return the maximum number of invitations that can be accepted.
"""

def maximumInvitations(grid, preferences):
    m, n = len(grid), len(grid[0])
    pref = [[n]*m for _ in range(m)]
    match_g = [0]*n
    match_b = [0]*n

    def ofs(x):
        for y in preferences[x]:
            if visit[y] == 0:
                visit[y] = 1
                if match_g[y] == -1 or not ofs(match_g[y]):
                    match_b[x] = y
                    match_g[y] = x
                    return True
        return False

    matched = 0
    for x in range(m):
        for y in preferences[x]:
            if grid[x][y] == 1:
                pref[y][x] = True

    for x in range(m):
        visit = [0]*n
        if ofs(x):
            matched += 1
    return matched