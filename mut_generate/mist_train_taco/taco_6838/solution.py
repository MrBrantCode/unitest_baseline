"""
QUESTION:
Woken up by the alarm clock Igor the financial analyst hurried up to the work. He ate his breakfast and sat in his car. Sadly, when he opened his GPS navigator, he found that some of the roads in Bankopolis, the city where he lives, are closed due to road works. Moreover, Igor has some problems with the steering wheel, so he can make no more than two turns on his way to his office in bank.

Bankopolis looks like a grid of n rows and m columns. Igor should find a way from his home to the bank that has no more than two turns and doesn't contain cells with road works, or determine that it is impossible and he should work from home. A turn is a change in movement direction. Igor's car can only move to the left, to the right, upwards and downwards. Initially Igor can choose any direction. Igor is still sleepy, so you should help him.

Input

The first line contains two integers n and m (1 ≤ n, m ≤ 1000) — the number of rows and the number of columns in the grid.

Each of the next n lines contains m characters denoting the corresponding row of the grid. The following characters can occur: 

  * "." — an empty cell; 
  * "*" — a cell with road works; 
  * "S" — the cell where Igor's home is located; 
  * "T" — the cell where Igor's office is located. 



It is guaranteed that "S" and "T" appear exactly once each.

Output

In the only line print "YES" if there is a path between Igor's home and Igor's office with no more than two turns, and "NO" otherwise.

Examples

Input

5 5
..S..
****.
T....
****.
.....


Output

YES

Input

5 5
S....
****.
.....
.****
..T..


Output

NO

Note

The first sample is shown on the following picture:

<image>

In the second sample it is impossible to reach Igor's office using less that 4 turns, thus there exists no path using no more than 2 turns. The path using exactly 4 turns is shown on this picture:

<image>
"""

def can_igor_reach_office(n, m, grid):
    def run(r, c, visited):
        visited[r][c] = True
        for i in range(c + 1, m + 2):
            if visited[r][i] or not ok[r][i]:
                break
            visited[r][i] = True
        for i in range(c - 1, -1, -1):
            if visited[r][i] or not ok[r][i]:
                break
            visited[r][i] = True
        for i in range(r + 1, n + 2):
            if visited[i][c] or not ok[i][c]:
                break
            visited[i][c] = True
        for i in range(r - 1, -1, -1):
            if visited[i][c] or not ok[i][c]:
                break
            visited[i][c] = True

    ok = [[False] * (m + 2)]
    for i in range(n):
        ok.append([False] + [True if ch != '*' else False for ch in grid[i]] + [False])
        if 'S' in grid[i]:
            start = (i + 1, grid[i].find('S') + 1)
        if 'T' in grid[i]:
            goal = (i + 1, grid[i].find('T') + 1)
    ok.append([False] * (m + 2))

    visited = [[False] * (m + 2) for i in range(n + 2)]
    visited[start[0]][start[1]] = True
    run(start[0], start[1], visited)

    visited1 = [[False] * (m + 2) for i in range(n + 2)]
    for i in range(n + 2):
        for j in range(m + 2):
            if visited[i][j]:
                run(i, j, visited1)

    visited2 = [[False] * (m + 2) for i in range(n + 2)]
    for i in range(n + 2):
        for j in range(m + 2):
            if visited1[i][j]:
                run(i, j, visited2)

    return 'YES' if visited2[goal[0]][goal[1]] else 'NO'