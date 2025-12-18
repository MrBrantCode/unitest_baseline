"""
QUESTION:
There are $n$ points $1,2,\ldots,n$, each point $i$ has a number $a_i$ on it. You're playing a game on them. Initially, you are at point $1$. When you are at point $i$, take following steps:

If $1\le i\le n$, go to $i+a_i$,

Otherwise, the game ends.

Before the game begins, you can choose two integers $x$ and $y$ satisfying $1\le x\le n$, $-n \le y \le n$ and replace $a_x$ with $y$ (set $a_x := y$). Find the number of distinct pairs $(x,y)$ such that the game that you start after making the change ends in a finite number of steps.

Notice that you do not have to satisfy $a_x\not=y$.


-----Input-----

Each test contains multiple test cases. The first line contains an integer $t$ ($1\le t\le 10^4)$ — the number of test cases.

The first line of each test case contains one integer $n$ ($1\le n\le 2\cdot 10^5$) — the number of points.

The second line contains $n$ integers $a_1,a_2,\ldots,a_n$ ($-n \le a_i \le n$) — the numbers on the axis.

It's guaranteed that the sum of $n$ does not exceed $2\cdot 10^5$.


-----Output-----

For each test case, print a line containing a single integer — the number of distinct pairs $(x,y)$ with which the game ends.


-----Examples-----

Input
9
1
0
2
-1 0
2
1 -1
2
1 1
3
-1 -2 -1
3
1 -2 -1
4
-1 4 -2 1
5
1 1 1 1 -4
5
1 1 1 1 1
Output
2
8
6
7
20
17
34
30
40


-----Note-----

In the first test case, the pairs $(x,y)$ with which the game ends are $(1,-1)$ and $(1,1)$, corresponding to the routes $1\rightarrow 0$ and $1\rightarrow 2$. Note that $(1,2)$ is invalid since when $n=1$, $y=2$ violates $-n\le y\le n$. $(1,0)$ is also invalid since you will go from $1$ to $1$ forever.

In the second test case, the pairs are $(1,-2),(1,-1),(1,2),(2,-2),(2,-1),(2,0),(2,1),(2,2)$.

In the fourth test case, the pairs are $(1,-2),(1,-1),(1,1),(1,2),(2,-2),(2,1),(2,2)$.
"""

def count_finite_game_pairs(n, a):
    ans = n * (n * 2 + 1)
    visited = [0] * n
    path = []
    pt = 0
    flag = False
    
    while not visited[pt]:
        path.append(pt)
        visited[pt] = 1
        pt += a[pt]
        if not 0 <= pt < n:
            break
    else:
        ans -= (n - sum(visited)) * (2 * n + 1)
        flag = True
    
    cnt = sum(visited)
    if flag:
        ans -= cnt * cnt
    else:
        ans -= (1 + cnt) * cnt // 2
    
    new_visited = [0] * n
    note = visited[:]
    
    for i in range(n):
        if not note[i]:
            tmp = []
            f = False
            while not note[i]:
                tmp.append(i)
                note[i] = 1
                i += a[i]
                if not 0 <= i < n:
                    break
                if note[i] and new_visited[i] >= 0 or visited[i]:
                    f = True
            if f:
                if new_visited[i]:
                    i = new_visited[i] - 1
                for x in tmp:
                    new_visited[x] = i + 1
            else:
                for x in tmp:
                    new_visited[x] = -1
    
    path_note = {v: i for (i, v) in enumerate(path)}
    
    for i in range(n):
        if not visited[i]:
            if new_visited[i] != -1:
                if visited[new_visited[i] - 1] == 0 or flag:
                    ans -= cnt
                else:
                    ans -= cnt - path_note[new_visited[i] - 1]
    
    return ans