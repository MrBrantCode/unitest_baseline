"""
QUESTION:
There are $n$ persons who initially don't know each other. On each morning, two of them, who were not friends before, become friends.

We want to plan a trip for every evening of $m$ days. On each trip, you have to select a group of people that will go on the trip. For every person, one of the following should hold:   Either this person does not go on the trip,  Or at least $k$ of his friends also go on the trip. 

Note that the friendship is not transitive. That is, if $a$ and $b$ are friends and $b$ and $c$ are friends, it does not necessarily imply that $a$ and $c$ are friends.

For each day, find the maximum number of people that can go on the trip on that day.


-----Input-----

The first line contains three integers $n$, $m$, and $k$ ($2 \leq n \leq 2 \cdot 10^5, 1 \leq m \leq 2 \cdot 10^5$, $1 \le k < n$) — the number of people, the number of days and the number of friends each person on the trip should have in the group.

The $i$-th ($1 \leq i \leq m$) of the next $m$ lines contains two integers $x$ and $y$ ($1\leq x, y\leq n$, $x\ne y$), meaning that persons $x$ and $y$ become friends on the morning of day $i$. It is guaranteed that $x$ and $y$ were not friends before.


-----Output-----

Print exactly $m$ lines, where the $i$-th of them ($1\leq i\leq m$) contains the maximum number of people that can go on the trip on the evening of the day $i$.


-----Examples-----
Input
4 4 2
2 3
1 2
1 3
1 4

Output
0
0
3
3

Input
5 8 2
2 1
4 2
5 4
5 2
4 3
5 1
4 1
3 2

Output
0
0
0
3
3
4
4
5

Input
5 7 2
1 5
3 2
2 5
3 4
1 2
5 3
1 3

Output
0
0
0
0
3
4
4



-----Note-----

In the first example,   $1,2,3$ can go on day $3$ and $4$. 

In the second example,   $2,4,5$ can go on day $4$ and $5$.  $1,2,4,5$ can go on day $6$ and $7$.  $1,2,3,4,5$ can go on day $8$. 

In the third example,   $1,2,5$ can go on day $5$.  $1,2,3,5$ can go on day $6$ and $7$.
"""

from collections import deque

def max_trip_sizes(n, m, k, friendships):
    adj = [set() for _ in range(n)]
    uv = []
    
    for u, v in friendships:
        adj[u - 1].add(v - 1)
        adj[v - 1].add(u - 1)
        uv.append((u - 1, v - 1))
    
    nn = [len(a) for a in adj]
    q = deque()
    
    for i in range(n):
        if nn[i] < k:
            q.append(i)
    
    while q:
        v = q.popleft()
        for u in adj[v]:
            nn[u] -= 1
            if nn[u] == k - 1:
                q.append(u)
    
    res = [0] * m
    nk = len([1 for i in nn if i >= k])
    res[-1] = nk
    
    for i in range(m - 1, 0, -1):
        u1, v1 = uv[i]
        if nn[u1] < k or nn[v1] < k:
            res[i - 1] = nk
            continue
        if nn[u1] == k:
            q.append(u1)
            nn[u1] -= 1
        if not q and nn[v1] == k:
            q.append(v1)
            nn[v1] -= 1
        if not q:
            nn[u1] -= 1
            nn[v1] -= 1
            adj[u1].remove(v1)
            adj[v1].remove(u1)
        while q:
            v = q.popleft()
            nk -= 1
            for u in adj[v]:
                nn[u] -= 1
                if nn[u] == k - 1:
                    q.append(u)
        res[i - 1] = nk
    
    return res