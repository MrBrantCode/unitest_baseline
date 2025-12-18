"""
QUESTION:
There is a city with $N$ numbered $0 - N-1$ shops. A market is a place where we can reach from one shop to another using some road. There are $M$ roads in this city connecting each connecting any two shops. 
Find the number of markets in the city.
NOTE:  A market having only one shop is also a valid market.

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- First line of Each Test Case is $N, M$, denoting the number of shops and the number of roads respectively.
- Next M lines consist of two integers $A$ and $B$ denoting that there exists a road between Shop A and Shop B

-----Output:-----
For each testcase, output the number of markets.

-----Constraints-----
- $1 \leq T \leq 100$
- $1 \leq N,M \leq 10^3$
- $0 \leq A,B < N$

-----Sample Input:-----
1
5 3
0 1
2 3
3 4

-----Sample Output:-----
2
"""

def count_markets(T, test_cases):
    def dfs(src, visit):
        visit[src] = 1
        for nbr in d[src]:
            if visit[nbr] == 0:
                dfs(nbr, visit)

    results = []
    for case in test_cases:
        N, M, roads = case
        d = {}
        for u, v in roads:
            if u in d:
                d[u].append(v)
            else:
                d[u] = [v]
            if v in d:
                d[v].append(u)
            else:
                d[v] = [u]
        visited = {i: 0 for i in range(N)}
        ans = 0
        for i in range(N):
            if visited[i] == 0:
                ans += 1
                if i in d:
                    dfs(i, visited)
        results.append(ans)
    return results