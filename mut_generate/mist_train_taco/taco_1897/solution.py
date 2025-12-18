"""
QUESTION:
An intergallactic war is on. Aliens are throwing fire-balls at our planet and this fire is so deadly that whichever nation it hits, it will wipe out not only that nation, but also spreads to any other nation which lies adjacent to it. 

Given an NxM map which has N x M cells. Each cell may have a country or else it may be the ocean. Fire cannot penetrate the ocean or go beyond the edges of the map (a wise man managed to bound the corners preventing fire from wrapping around the corners). 

You will be given a initial state of the planet represented by an N x M grid consists of 0 or 1 representing ocean and nation respectively. Also there will be Q attacks of the fire-ball. After each query, you are to tell the number of nations still left unburnt.

Input:
First line of input contains 3 space separated integers N,M,Q where N x M is the size of the planet. Q is the number of fire-ball attacks. N lines follow each with M values of either 0 or 1, denoting whether that particular coordinate is a nation(1) or ocean(0). 
Q lines follow. Each line has a coordinate X,Y where the next fire-ball attack takes place.

Output:
For each Q, output the number of nations still existing on a single line.
Note:

 Two countries are said to be adjacent if they share an edge.
 Aliens can shoot the fireball at any place on the planet within its domain any number of times. 
 Once a nation is destroyed, it will continue to remain destroyed over all the forthcoming queries. 
 Large IO. Prefer scanf/printf(in C/C++). 
Constraints:

1 ≤ N,M ≤ 10^3
1 ≤ X ≤ N
1 ≤ Y ≤ M
1 ≤ Q ≤ 10^6

Scoring:

1 ≤ N,M ≤ 10^2 , Q ≤ 10^3: (30 pts)
Original Constraints : (70 pts)

SAMPLE INPUT
3 3 3
0 0 0
1 0 1
0 1 1
1 2
2 2
3 3

SAMPLE OUTPUT
4
4
1

Explanation

Query 1: (1,2) No nation is hit. Unburnt nations=4 (initial)
Query 2: (2,2) No nation is hit. Still unburnt=4
Query 3: (3,3) is hit and fire spreads to (2,3) and (3,2) also. Thus only 1 nation is left (1,2).
"""

def calculate_unburnt_nations(N, M, Q, grid, attacks):
    def valid(x, y):
        return y >= 0 and x >= 0 and y < M and x < N

    def dfs(start):
        nonlocal component_id
        c = 1
        q = [start]
        
        while q:
            top = q.pop(0)
            parent[top[0]][top[1]] = component_id
            mark[top[0]][top[1]] = True
            
            for k in dif:
                if (valid(top[0] + k[0], top[1] + k[1])) and (grid[top[0] + k[0]][top[1] + k[1]] == "1") and mark[top[0] + k[0]][top[1] + k[1]] == False:
                    mark[top[0] + k[0]][top[1] + k[1]] = True
                    parent[top[0] + k[0]][top[1] + k[1]] = component_id
                    c += 1
                    q.append((top[0] + k[0], top[1] + k[1]))
        
        return c

    dif = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, upward, right, left (i, j)
    mark = [[False for _ in range(M)] for _ in range(N)]
    parent = [[0 for _ in range(M)] for _ in range(N)]
    component_id = 1
    co = 0
    d = {}
    f = {}

    for i in range(N):
        for j in range(M):
            if grid[i][j] == "1":
                co += 1
                if mark[i][j] == False:
                    tI = dfs((i, j))
                    d[component_id] = tI
                    f[component_id] = True
                    component_id += 1

    results = []
    for x, y in attacks:
        if grid[x-1][y-1] == "0":
            results.append(co)
        else:
            if f[parent[x-1][y-1]] == True:
                co = co - d[parent[x-1][y-1]]
                f[parent[x-1][y-1]] = False
                results.append(co)
            else:
                results.append(co)
    
    return results