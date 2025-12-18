"""
QUESTION:
Reverse_flash lost his power while moving through a number of timezones and landed in the timezone of Flash. Now we know that Flash would kill him as soon as he finds him.
Your job is to protect the bad.
The timezone of Flash is  (1,1). There is a safe timezone (n,n), the last one ,where Flash couldn't enter.
Timezone which Reverse_flash could pass through/enter is represented by 0 and which he couldn't is represented by 1.Now your task to find the possible number of ways to reach timezone (n,n) from (1,1).
Input format & constraints
1st line --> integer value 'n'  (n ≤ 100) denoting the size of the grid of timezones.
Next n lines -->each line contains n space separated integers either 1 or 0.
Output format
A line with possible number of ways you could protect bad from good i.e, all possible ways you could make him reach (n,n) from (1,1).
Note Reverse_Flash could only move either horizontally or vertically i.e, not diagonally :)

SAMPLE INPUT
7
0 0 0 0 0 0 0
0 1 0 1 0 1 0
0 0 0 0 0 0 0
0 1 0 1 0 1 0
0 0 0 0 0 0 0
0 1 0 1 0 1 0
0 0 0 0 0 0 0

SAMPLE OUTPUT
184
"""

def count_ways_to_reach_end(n, time_zone):
    def s(r, c):
        nonlocal ans
        if r == n-1 and c == n-1:
            ans += 1
            return
        vis[r][c] = True
        for i in range(4):
            nr = r + steps[i][0]
            nc = c + steps[i][1]
            
            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                continue
            if vis[nr][nc] or time_zone[nr][nc] == 1:
                continue
            s(nr, nc)
            vis[nr][nc] = False
    
    ans = 0
    vis = [[False for _ in range(n)] for _ in range(n)]
    steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    s(0, 0)
    return ans