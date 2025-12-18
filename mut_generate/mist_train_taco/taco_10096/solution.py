"""
QUESTION:
Description

F, who likes to dance, decided to practice a hardcore dance called JUMP STYLE at a certain dance hall.

The floor is tiled in an N × N grid. To support the dance practice, each tile has the coordinates of the tile to jump to the next step. F has strong motor nerves through daily practice and can jump to any tile on the floor.

F realized that if he continued this dance for a long enough time, he would eventually enter a steady state and just loop on the same route. F wondered how many such loops existed on this floor and decided to talk to you, the programmer.



Input

The input consists of multiple test cases.

Each test case begins with one line containing the length N of one side of the floor. (1 ≤ N ≤ 100)

The following N lines represent the coordinates of the jump destination written on each tile on the floor as follows.


\\ begin {array} {ccccccc}
x_ {0,0} & y_ {0,0} & x_ {1,0} & y_ {1,0} & \\ cdots & x_ {N-1,0} & y_ {N-1,0} \ \\\
x_ {0,1} & y_ {0,1} & x_ {1,1} & y_ {1,1} & \\ cdots & x_ {N-1,1} & y_ {N-1,1} \ \\\
\\ vdots & \\ vdots & \\ vdots & \\ vdots & \\ ddots & \\ vdots & \\ vdots \\\\
x_ {0, N-1} & y_ {0, N-1} & x_ {1, N-1} & y_ {1, N-1} & \\ cdots & x_ {N-1, N-1} & y_ {N-1, N-1}
\\ end {array}


x_ {i, j} and \\ y_ {i, j} represent the x-coordinate and y-coordinate of the jump destination written on the tile at the coordinate (i, j), respectively. The coordinates are 0-origin, and the values ​​of all coordinates are integers greater than or equal to 0 and less than N.

The input ends with a line consisting of only 0s.

Output

For each test case, the number of different loops is output in one line.

Example

Input

1
0 0
2
1 1 0 1
1 0 0 0
2
1 1 0 1
1 1 1 0
3
0 1 2 2 2 1
0 2 1 2 2 1
0 0 0 1 1 1
4
3 2 2 0 3 2 2 1
1 1 0 3 1 1 3 1
0 3 2 3 3 0 2 3
1 1 1 1 3 2 1 3
0


Output

1
2
1
2
3
"""

def count_dance_loops(n, jump_destinations):
    to = []
    fr = [[] for _ in range(n * n)]
    
    for i in range(n):
        for j in range(n):
            x, y = jump_destinations[i][2 * j], jump_destinations[i][2 * j + 1]
            to.append(y * n + x)
            fr[y * n + x].append(i * n + j)
    
    order = []
    used = [False] * (n * n)
    
    def dfs(x):
        if used[x]:
            return
        used[x] = True
        dfs(to[x])
        order.append(x)
    
    for i in range(n * n):
        dfs(i)
    
    def dfs2(x, used, group):
        if used[x]:
            return
        used[x] = True
        for f in fr[x]:
            dfs2(f, used, group)
        group.append(x)
    
    used = [False] * (n * n)
    ans = 0
    
    for i in order:
        group = []
        if not used[i]:
            dfs2(i, used, group)
        if len(group) >= 1:
            ans += 1
    
    return ans