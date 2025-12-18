"""
QUESTION:
Demiurges Shambambukli and Mazukta love to watch the games of ordinary people. Today, they noticed two men who play the following game.

There is a rooted tree on n nodes, m of which are leaves (a leaf is a nodes that does not have any children), edges of the tree are directed from parent to children. In the leaves of the tree integers from 1 to m are placed in such a way that each number appears exactly in one leaf.

Initially, the root of the tree contains a piece. Two players move this piece in turns, during a move a player moves the piece from its current nodes to one of its children; if the player can not make a move, the game ends immediately. The result of the game is the number placed in the leaf where a piece has completed its movement. The player who makes the first move tries to maximize the result of the game and the second player, on the contrary, tries to minimize the result. We can assume that both players move optimally well.

Demiurges are omnipotent, so before the game they can arbitrarily rearrange the numbers placed in the leaves. Shambambukli wants to rearrange numbers so that the result of the game when both players play optimally well is as large as possible, and Mazukta wants the result to be as small as possible. What will be the outcome of the game, if the numbers are rearranged by Shambambukli, and what will it be if the numbers are rearranged by Mazukta? Of course, the Demiurges choose the best possible option of arranging numbers.


-----Input-----

The first line contains a single integer n — the number of nodes in the tree (1 ≤ n ≤ 2·10^5).

Each of the next n - 1 lines contains two integers u_{i} and v_{i} (1 ≤ u_{i}, v_{i} ≤ n) — the ends of the edge of the tree; the edge leads from node u_{i} to node v_{i}. It is guaranteed that the described graph is a rooted tree, and the root is the node 1.


-----Output-----

Print two space-separated integers — the maximum possible and the minimum possible result of the game.


-----Examples-----
Input
5
1 2
1 3
2 4
2 5

Output
3 2

Input
6
1 2
1 3
3 4
1 5
5 6

Output
3 3



-----Note-----

Consider the first sample. The tree contains three leaves: 3, 4 and 5. If we put the maximum number 3 at node 3, then the first player moves there and the result will be 3. On the other hand, it is easy to see that for any rearrangement the first player can guarantee the result of at least 2.

In the second sample no matter what the arragment is the first player can go along the path that ends with a leaf with number 3.
"""

def calculate_game_results(n, edges):
    g = [[] for _ in range(n + 1)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    
    q = [1]
    d = [None] * (n + 1)
    d[1] = 0
    i = 0
    
    while i < len(q):
        x = q[i]
        i += 1
        for v in g[x]:
            if d[v] is None:
                q.append(v)
                d[v] = d[x] + 1
                g[v].remove(x)
    
    m = [0] * (n + 1)
    M = [0] * (n + 1)
    cnt = 0
    
    for i in range(len(q) - 1, -1, -1):
        x = q[i]
        if len(g[x]) == 0:
            m[x] = 1
            M[x] = 1
            cnt += 1
        elif d[x] % 2 == 0:
            c = 0
            C = int(1000000000.0)
            for v in g[x]:
                c += m[v]
            for v in g[x]:
                C = min(C, M[v])
            m[x] = c
            M[x] = C
        else:
            c = int(1000000000.0)
            C = 0
            for v in g[x]:
                c = min(c, m[v])
            for v in g[x]:
                C += M[v]
            m[x] = c
            M[x] = C
    
    return (cnt + 1 - M[x], m[1])