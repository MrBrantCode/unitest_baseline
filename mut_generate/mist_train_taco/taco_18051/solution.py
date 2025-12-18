"""
QUESTION:
Alice and Bob are playing a game, defined below:

There is an undirected tree graph with $n$ nodes that has the following properties: 
Each node has $c_i$ golden coins. 
Node $\mbox{1}$ is root of the tree. 
The parent node of some node $\mbox{u}$ is defined as $p(u)$.
Moves
Players move in turns. 
During a move, a player can select a node $u>1$ and move one or more coins to $p(u)$. 
If the current player can't make any move, they lose the game.

The game quickly becomes boring because the result is determined by the tree's configuration and the number of coins in each node (assuming that both players play optimally).

Alice decides to instead challenge Bob by asking him $\textit{q}$ questions. For each question $\boldsymbol{i}$:

Alice picks a node $u_i>1$ and removes the edge between $u_i$ and $p(u_i)$. 
She picks another node $\boldsymbol{\nu}$ and draws a new undirected edge between $u_i$ and $v_i$. So now $p(u_i)=v_i$.

Bob must determine if the first player has a winning strategy for the new tree or not. It's possible that after Alice draws the new edge, the graph will no longer be a tree; if that happens, the question is invalid. Each question is independent, so the answer depends on the initial state of the graph (and not on previous questions).

Given the tree and the number of coins in each node, can you help Bob answer all $\textit{q}$ questions?

Input Format

The first line contains an integer, $n$ (the number of nodes). 

The second line contains $n$ space-separated integers, $c_1,c_2,\ldots,c_n$, describing the number of coins in each node. 

Each of the $n-1$ subsequent lines contains $2$ space-separated integers denoting an undirected edge between nodes $\boldsymbol{a}$ and $\boldsymbol{b}$, respectively. 

The next line contains an integer, $\textit{q}$ (the number of questions Alice asks). 

Each of the $\textit{q}$ subsequent lines contains $2$ space-separated integers, $u_i$ and $v_i$, respectively.

Constraints

$1\leq n,q\leq5\times10^4$
$1\leq a,b\leq n$
$0\leq c_i\leq20$

For each question:

$2\leq u_i\leq n$
$1\leq v_i\leq n$
$u_i\neq v_i$

Output Format

On a new line for each question, print $\mathtt{YES}$ if the first player has a winning strategy, print $\boldsymbol{\textbf{NO}}$ if they do not, or print $\textbf{INVALID}$ if the question is not valid.

Sample Input
6
0 2 2 1 3 2
1 2
1 3
3 4
3 5
4 6
3
6 2
4 1
3 6

Sample Output
NO
YES
INVALID

Explanation

Initally the tree looks like this:

After the first question (${6\:\:2}$), the tree looks like this:

Alice removes the edge conecting node $\boldsymbol{6}$ to $\begin{array}{c}4\end{array}$ and makes $2$ the new parent node of $\boldsymbol{6}$. Because this configuration does not result in a winning strategy, we print $\boldsymbol{\textbf{NO}}$ on a new line.

After the second question (${4\:\:1}$), the tree looks like this:

Alice removes the edge conecting node $\begin{array}{c}4\end{array}$ to $3$ and makes $\mbox{1}$ the new parent node of $\begin{array}{c}4\end{array}$. Because this configuration results in a winning strategy, we print $\mathtt{YES}$ on a new line.

After the third question (${3\:\:6}$), the graph is no longer a tree:

Alice removes the edge conecting node $3$ to $\mbox{1}$ and makes $\boldsymbol{6}$ the new parent node of $3$. The graph is now partitioned into two separate subgraphs (one of which is also not a tree); because the game must be played on a single undirected tree graph, we print $\textbf{INVALID}$ on a new line.
"""

from collections import deque

def determine_winning_strategy(n, coins, edges, questions):
    G = [[int(c), 0, []] for c in coins]
    G[0][2].append(0)
    parity = [True for _ in range(n)]
    order = [[-1, -1] for _ in range(n)]
    
    for v1, v2 in edges:
        G[v1 - 1][2].append(v2 - 1)
        G[v2 - 1][2].append(v1 - 1)
    
    total = 0
    pre = 0
    post = 0
    parent = deque([0])
    
    while len(parent) > 0:
        node = parent.pop()
        if order[node][0] == -1:
            order[node][0] = pre
            pre += 1
            parity[node] = not parity[G[node][1]]
            if parity[node]:
                total = total ^ G[node][0]
            G[node][2].remove(G[node][1])
            if len(G[node][2]) == 0:
                parent.append(node)
            else:
                for c in G[node][2]:
                    G[c][1] = node
                    parent.append(c)
        else:
            order[node][1] = post
            post += 1
            for c in G[node][2]:
                G[node][0] = G[node][0] ^ G[c][0]
            if G[G[node][1]][2][0] == node:
                parent.append(G[node][1])
    
    results = []
    for u, v in questions:
        u -= 1
        v -= 1
        if order[u][0] < order[v][0] and order[u][1] > order[v][1]:
            results.append('INVALID')
        elif parity[u] == parity[v]:
            newtotal = G[u][0]
            if newtotal ^ total == 0:
                results.append('NO')
            else:
                results.append('YES')
        elif total == 0:
            results.append('NO')
        else:
            results.append('YES')
    
    return results