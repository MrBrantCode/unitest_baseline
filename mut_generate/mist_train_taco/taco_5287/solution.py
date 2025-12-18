"""
QUESTION:
Alice and Bob are playing a game with a rooted tree. The tree has $N$ vertices and the first node, $1$, is always the root. Here are the basic rules:

They move in alternating turns, and both players always move optimally.
During each move, a player removes an edge from the tree, disconnecting one of its leaves or branches. The leaf or branch that was disconnected from the rooted tree is removed from the game. 
The first player to be unable to make a move loses the game.
Alice always makes the first move. 

For example, the diagram below shows a tree of size $n=7$, where the root is node $1$:

Now, if a player removes the edge between $1$ and $4$, then nodes $4$ and $7$ become disconnected from the root and are removed from the game:

Given the structure of the tree, determine and print the winner of the game. If Alice wins, print $\textbf{Alice}$; otherwise print $\textbf{Bob}$.

Input Format

The first line contains a single integer, $\mathbf{T}$, denoting the number of test cases. 

For each test case, the first line contains an integer, $N$, denoting the number of nodes in the tree. 

Each of the $N-1$ subsequent lines contains $2$ space-separated integers, $\mbox{u}$ and $v$, defining an edge connecting nodes $\mbox{u}$ and $v$.

Constraints

$1\leq T\leq100$
$1\leq N\leq500$
$1\leq u,v\leq N$

Output Format

For each test case, print the name of the winner (i.e., $\textbf{Alice}$ or $\textbf{Bob}$) on a new line.

Sample Input
1
5
1 2
3 1
3 4
4 5

Sample Output
Alice

Explanation

Test Case 0:

Alice removes the edge connecting node $3$ to node $4$, effectively trimming nodes $4$ and $5$ from the tree. Now the only remaining edges are $1\leftrightarrow2$ and $1\leftrightarrow3$. Because Bob can't remove both of them, Alice will make the last possible move. Because the last player to move wins, we print $\textbf{Alice}$ on a new line.
"""

def determine_game_winners(T, test_cases):
    def hackenbush(i, p, g):
        v = 0
        for x in g[i]:
            if x == p:
                continue
            v = v ^ hackenbush(x, i, g) + 1
        return v

    results = []
    for case in test_cases:
        N, edges = case
        g = {i: [] for i in range(1, N + 1)}
        for (a, b) in edges:
            g[a].append(b)
            g[b].append(a)
        if hackenbush(1, 0, g):
            results.append('Alice')
        else:
            results.append('Bob')
    return results