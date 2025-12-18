"""
QUESTION:
You are given a graph with $n$ nodes and $m$ directed edges. One lowercase letter is assigned to each node. We define a path's value as the number of the most frequently occurring letter. For example, if letters on a path are "abaca", then the value of that path is $3$. Your task is find a path whose value is the largest.


-----Input-----

The first line contains two positive integers $n, m$ ($1 \leq n, m \leq 300\,000$), denoting that the graph has $n$ nodes and $m$ directed edges.

The second line contains a string $s$ with only lowercase English letters. The $i$-th character is the letter assigned to the $i$-th node.

Then $m$ lines follow. Each line contains two integers $x, y$ ($1 \leq x, y \leq n$), describing a directed edge from $x$ to $y$. Note that $x$ can be equal to $y$ and there can be multiple edges between $x$ and $y$. Also the graph can be not connected.


-----Output-----

Output a single line with a single integer denoting the largest value. If the value can be arbitrarily large, output -1 instead.


-----Examples-----
Input
5 4
abaca
1 2
1 3
3 4
4 5

Output
3

Input
6 6
xzyabc
1 2
3 1
2 3
5 4
4 3
6 4

Output
-1

Input
10 14
xzyzyzyzqx
1 2
2 4
3 5
4 5
2 6
6 8
6 5
2 10
3 9
10 9
4 6
1 10
2 8
3 7

Output
4



-----Note-----

In the first sample, the path with largest value is $1 \to 3 \to 4 \to 5$. The value is $3$ because the letter 'a' appears $3$ times.
"""

from collections import defaultdict, deque

def find_largest_path_value(n, m, s, edges):
    deg = [0 for _ in range(n)]
    graph = defaultdict(list)
    
    for (a, b) in edges:
        a -= 1
        b -= 1
        graph[a].append(b)
        deg[b] += 1
    
    q = deque()
    for i in range(n):
        if deg[i] == 0:
            q.append(i)
    
    count = 0
    dp = [[0 for _ in range(26)] for _ in range(n)]
    
    while count < n and q:
        und = q.popleft()
        count += 1
        dp[und][ord(s[und]) - 97] += 1
        for i in graph[und]:
            for j in range(26):
                dp[i][j] = max(dp[i][j], dp[und][j])
            deg[i] -= 1
            if deg[i] == 0:
                q.append(i)
    
    if count != n:
        return -1
    
    ans = 0
    for i in range(n):
        ans = max(ans, max(dp[i]))
    
    return ans