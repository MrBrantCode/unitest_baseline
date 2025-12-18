"""
QUESTION:
Bob and Ben are playing a game with forests! The game's rules are as follows:

The game starts with a forest of $n$ trees.
Bob always moves first and they take alternating turns. The first player with no available move loses the game.
During each move, the player removes one node. If the node is not a leaf, then the whole tree vanishes; otherwise, the rest of the tree remains in the forest. We define a leaf to be a node with exactly $1$ connected edge.
Both players play optimally, meaning they will not make a move that causes them to lose the game if some better, winning move exists.

We define each tree $\boldsymbol{i}$ in the $n$-tree forest as follows:

Tree $\boldsymbol{i}$ is defined by two integers, $m_i$ (the number of nodes in the tree) and $k_i$ (a constant). 
Its nodes are numbered sequentially from $1$ to $m_i$.
Its edges are numbered sequentially from $1$ to $m_i-1$, and each edge $j$ connects node $j+1$ to node $\lfloor\max(1,\frac{j}{k_i})\rfloor$.

Given the values of $m_i$ and $k_i$ for each tree in the forest, can you determine who will win the game?

Input Format

The first line contains an integer, $\mathrm{~g~}$, denoting the number of games. The subsequent lines describe each game in the following format:

The first line contains an integer, $g$, denoting the number of trees in the forest.     
Each of the $n$ subsequent lines contains two space-separated integers describing the respective values of $m_i$ and $k_i$ for tree $\boldsymbol{i}$. 

Constraints

$1\leq g\leq100$
$1\leq n\leq10^{6}$
$1\leq m_i\leq10^9$
$2\leq k_i\leq100$
The sum of $n$ over all games is at most $10^{6}$.

Subtasks

For $50\%$ of the maximum score:

The sum of $n$ over all games is at most $10^3$.
$1\leq m_i\leq10^3$

For $25\%$ of the maximum score:

$1\leq n,m_i,g\leq10$

Output Format

For each game, print the name of the winner on a new line (i.e., BOB or BEN).

Sample Input
2
2
1 2
1 3
1
3 2

Sample Output
BEN
BOB

Explanation

Bob and Ben play the following two games:

The forest consists of $n=2$ trees containing one node each, and each tree has no edges as $m_1$ and $m_2$ are both $\mbox{I}$ (so both trees have $1-1=0$ edges). The sequence of moves is as follows: 

We then print the name of the winner, BEN, on a new line.

The forest consists of $n=1$ tree containing three nodes. We find the $m_1-1=2$ edges like so: 

Edge $j=1$ connects node $j+1=2$ to node $floor(max(1,\frac{j}{k_1}))=floor(max(1,\frac{1}{2}))=1$.
Edge $j=2$ connects node $j+1=3$ to node $floor(max(1,\frac{j}{k_2}))=floor(max(1,\frac{2}{2}))=1$.       

The game then plays out as follows: 

We then print the name of the winner, BOB, on a new line.
"""

def determine_winner(games):
    results = []
    
    for game in games:
        (ones, twos, rest) = (0, 0, 0)
        for (m, k) in game:
            if m == 1:
                ones += 1
            elif m == 2:
                twos += 1
            else:
                rest += m
        
        if (ones % 2, twos % 2, rest % 2, len(game) % 2) in [(1, 0, 1, 0), (0, 0, 0, 0), (1, 1, 1, 1), (0, 1, 0, 1)]:
            results.append('BEN')
        else:
            results.append('BOB')
    
    return results