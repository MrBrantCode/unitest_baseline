"""
QUESTION:
Bridge Removal

ICPC islands once had been a popular tourist destination. For nature preservation, however, the government decided to prohibit entrance to the islands, and to remove all the man-made structures there. The hardest part of the project is to remove all the bridges connecting the islands.

There are n islands and n-1 bridges. The bridges are built so that all the islands are reachable from all the other islands by crossing one or more bridges. The bridge removal team can choose any island as the starting point, and can repeat either of the following steps.

* Move to another island by crossing a bridge that is connected to the current island.
* Remove one bridge that is connected to the current island, and stay at the same island after the removal.



Of course, a bridge, once removed, cannot be crossed in either direction. Crossing or removing a bridge both takes time proportional to the length of the bridge. Your task is to compute the shortest time necessary for removing all the bridges. Note that the island where the team starts can differ from where the team finishes the work.

Input

The input consists of at most 100 datasets. Each dataset is formatted as follows.

> n
>  p2 p3 ... pn
>  d2 d3 ... dn

The first integer n (3 ≤ n ≤ 800) is the number of the islands. The islands are numbered from 1 to n. The second line contains n-1 island numbers pi (1 ≤ pi < i), and tells that for each i from 2 to n the island i and the island pi are connected by a bridge. The third line contains n-1 integers di (1 ≤ di ≤ 100,000) each denoting the length of the corresponding bridge. That is, the length of the bridge connecting the island i and pi is di. It takes di units of time to cross the bridge, and also the same units of time to remove it. Note that, with this input format, it is assured that all the islands are reachable each other by crossing one or more bridges.

The input ends with a line with a single zero.

Output

For each dataset, print the minimum time units required to remove all the bridges in a single line. Each line should not have any character other than this number.

Sample Input


4
1 2 3
10 20 30
10
1 2 2 1 5 5 1 8 8
10 1 1 20 1 1 30 1 1
3
1 1
1 1
0


Output for the Sample Input


80
136
2






Example

Input

4
1 2 3
10 20 30
10
1 2 2 1 5 5 1 8 8
10 1 1 20 1 1 30 1 1
3
1 1
1 1
0


Output

80
136
2
"""

def calculate_min_removal_time(n, P, D):
    from sys import setrecursionlimit
    setrecursionlimit(10 ** 8)

    E = [list() for _ in range(n + 1)]
    for (i, (p, c)) in enumerate(zip(P, D), 2):
        E[i].append((p, c))
        E[p].append((i, c))
    
    ans = 3 * sum(D)
    visited = [False] * (n + 1)
    is_leaf = [len(E[i]) == 1 for i in range(n + 1)]
    ans -= 2 * sum((E[i][0][1] for i in range(n + 1) if is_leaf[i]))

    def dfs(i):
        visited[i] = True
        res = 0
        for (e, c) in E[i]:
            if is_leaf[e] or visited[e]:
                continue
            res = max(res, dfs(e) + c)
        return res
    
    r = 0
    for i in range(1, n + 1):
        if is_leaf[i]:
            continue
        visited = [False] * (n + 1)
        r = max(r, dfs(i))
    
    return ans - r