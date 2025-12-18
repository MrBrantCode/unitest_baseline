"""
QUESTION:
The famous global economic crisis is approaching rapidly, so the states of Berman, Berance and Bertaly formed an alliance and allowed the residents of all member states to freely pass through the territory of any of them. In addition, it was decided that a road between the states should be built to guarantee so that one could any point of any country can be reached from any point of any other State.

Since roads are always expensive, the governments of the states of the newly formed alliance asked you to help them assess the costs. To do this, you have been issued a map that can be represented as a rectangle table consisting of n rows and m columns. Any cell of the map either belongs to one of three states, or is an area where it is allowed to build a road, or is an area where the construction of the road is not allowed. A cell is called passable, if it belongs to one of the states, or the road was built in this cell. From any passable cells you can move up, down, right and left, if the cell that corresponds to the movement exists and is passable.

Your task is to construct a road inside a minimum number of cells, so that it would be possible to get from any cell of any state to any cell of any other state using only passable cells.

It is guaranteed that initially it is possible to reach any cell of any state from any cell of this state, moving only along its cells. It is also guaranteed that for any state there is at least one cell that belongs to it.


-----Input-----

The first line of the input contains the dimensions of the map n and m (1 ≤ n, m ≤ 1000) — the number of rows and columns respectively.

Each of the next n lines contain m characters, describing the rows of the map. Digits from 1 to 3 represent the accessory to the corresponding state. The character '.' corresponds to the cell where it is allowed to build a road and the character '#' means no construction is allowed in this cell.


-----Output-----

Print a single integer — the minimum number of cells you need to build a road inside in order to connect all the cells of all states. If such a goal is unachievable, print -1.


-----Examples-----
Input
4 5
11..2
#..22
#.323
.#333
Output
2
Input
1 5
1#2#3

Output
-1
"""

from collections import deque

def calculate_minimum_road_cells(n, m, map_data):
    t = [set(), set(), set()]
    
    # Identify border cells for each state
    for i in range(n):
        for j in range(m):
            if map_data[i][j] in '123':
                for (ii, jj) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= ii < n and 0 <= jj < m:
                        if map_data[ii][jj] in '123.' and map_data[i][j] != map_data[ii][jj]:
                            t[int(map_data[i][j]) - 1].add((i, j))
                            break
    
    z = [[[1e+18] * 3 for j in range(m)] for i in range(n)]
    ans = 1e+18
    
    for root in range(3):
        q = deque()
        vi = [[False] * m for _ in range(n)]
        for (i, j) in t[root]:
            q.append((i, j, 0))
            vi[i][j] = True
            z[i][j][root] = 0
        dist = [1e+18] * 3
        dist[root] = 0
        
        while q:
            (i, j, d) = q.popleft()
            for (ii, jj) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ii < n and 0 <= jj < m and (not vi[ii][jj]):
                    if map_data[ii][jj] == '.':
                        vi[ii][jj] = True
                        q.append((ii, jj, d + 1))
                        z[ii][jj][root] = min(z[ii][jj][root], d + 1)
                    elif map_data[ii][jj] != map_data[i][j] and map_data[ii][jj] in '123':
                        dist[int(map_data[ii][jj]) - 1] = min(dist[int(map_data[ii][jj]) - 1], d)
        
        ans = min(ans, sum(dist))
    
    if ans >= 1e+18:
        return -1
    
    for i in range(n):
        for j in range(m):
            if map_data[i][j] == '.':
                ans = min(ans, sum(z[i][j]) - 2)
    
    return ans