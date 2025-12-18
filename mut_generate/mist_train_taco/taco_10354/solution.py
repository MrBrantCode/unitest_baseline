"""
QUESTION:
Nowadays the one-way traffic is introduced all over the world in order to improve driving safety and reduce traffic jams. The government of Berland decided to keep up with new trends. Formerly all n cities of Berland were connected by n two-way roads in the ring, i. e. each city was connected directly to exactly two other cities, and from each city it was possible to get to any other city. Government of Berland introduced one-way traffic on all n roads, but it soon became clear that it's impossible to get from some of the cities to some others. Now for each road is known in which direction the traffic is directed at it, and the cost of redirecting the traffic. What is the smallest amount of money the government should spend on the redirecting of roads so that from every city you can get to any other?

Input

The first line contains integer n (3 ≤ n ≤ 100) — amount of cities (and roads) in Berland. Next n lines contain description of roads. Each road is described by three integers ai, bi, ci (1 ≤ ai, bi ≤ n, ai ≠ bi, 1 ≤ ci ≤ 100) — road is directed from city ai to city bi, redirecting the traffic costs ci.

Output

Output single integer — the smallest amount of money the government should spend on the redirecting of roads so that from every city you can get to any other.

Examples

Input

3
1 3 1
1 2 1
3 2 1


Output

1


Input

3
1 3 1
1 2 5
3 2 1


Output

2


Input

6
1 5 4
5 3 8
2 4 15
1 6 16
2 3 23
4 6 42


Output

39


Input

4
1 2 9
2 3 8
3 4 7
4 1 5


Output

0
"""

def calculate_minimum_redirect_cost(n, roads):
    g = [[0] * (n + 1) for _ in range(n + 1)]
    d = [[0] * (n + 1) for _ in range(n + 1)]
    
    for a, b, c in roads:
        g[a][b] = c
        g[b][a] = c
        d[a][b] = c
        d[b][a] = -c
    
    ans = 0
    tot = 0
    stack = [1]
    visited = [1]
    
    while stack:
        t = stack.pop()
        for i in range(1, n + 1):
            if i not in visited and g[t][i] > 0:
                stack.append(i)
                visited.append(i)
                tot += g[t][i]
                if d[t][i] < 0:
                    ans += -d[t][i]
                break
    
    if d[visited[-1]][1] < 0:
        ans += -d[visited[-1]][1]
    tot += g[visited[-1]][1]
    visited.append(1)
    
    if ans > tot - ans:
        ans = tot - ans
    
    return ans