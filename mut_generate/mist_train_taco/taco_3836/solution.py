"""
QUESTION:
Snuke's town has a subway system, consisting of N stations and M railway lines. The stations are numbered 1 through N. Each line is operated by a company. Each company has an identification number.
The i-th ( 1 \leq i \leq M ) line connects station p_i and q_i bidirectionally. There is no intermediate station. This line is operated by company c_i.
You can change trains at a station where multiple lines are available.
The fare system used in this subway system is a bit strange. When a passenger only uses lines that are operated by the same company, the fare is 1 yen (the currency of Japan). Whenever a passenger changes to a line that is operated by a different company from the current line, the passenger is charged an additional fare of 1 yen. In a case where a passenger who changed from some company A's line to another company's line changes to company A's line again, the additional fare is incurred again.
Snuke is now at station 1 and wants to travel to station N by subway. Find the minimum required fare.

-----Constraints-----
 - 2 \leq N \leq 10^5
 - 0 \leq M \leq 2×10^5
 - 1 \leq p_i \leq N (1 \leq i \leq M)
 - 1 \leq q_i \leq N (1 \leq i \leq M)
 - 1 \leq c_i \leq 10^6 (1 \leq i \leq M)
 - p_i \neq q_i (1 \leq i \leq M)

-----Input-----
The input is given from Standard Input in the following format:
N M
p_1 q_1 c_1
:
p_M q_M c_M

-----Output-----
Print the minimum required fare. If it is impossible to get to station N by subway, print -1 instead.

-----Sample Input-----
3 3
1 2 1
2 3 1
3 1 2

-----Sample Output-----
1

Use company 1's lines: 1 → 2 → 3. The fare is 1 yen.
"""

from collections import deque

def calculate_minimum_fare(N, M, lines):
    inf = 10 ** 9
    to = []
    uctoi = {}
    
    # Initialize the adjacency list and the company-to-index mapping
    for u in range(N):
        to.append([])
        uctoi[u, 0] = u
    
    # Process each line to build the graph
    for (u, v, c) in lines:
        u -= 1
        v -= 1
        if (u, c) not in uctoi:
            i = uctoi[u, c] = len(to)
            to.append([])
            to[i].append(u)
            to[u].append(i)
        else:
            i = uctoi[u, c]
        if (v, c) not in uctoi:
            j = uctoi[v, c] = len(to)
            to.append([])
            to[j].append(v)
            to[v].append(j)
        else:
            j = uctoi[v, c]
        to[i].append(j)
        to[j].append(i)
    
    # Perform BFS to find the minimum fare
    dist = [inf] * len(to)
    q = deque()
    q.append((0, 0))
    dist[0] = 0
    
    while q:
        (d, i) = q.popleft()
        if d > dist[i]:
            continue
        if i < N:
            for j in to[i]:
                if dist[j] <= d + 1:
                    continue
                dist[j] = d + 1
                q.append((d + 1, j))
        else:
            for j in to[i]:
                if j == N - 1:
                    return dist[i]
                if dist[j] <= d:
                    continue
                dist[j] = d
                q.appendleft((d, j))
    
    return -1