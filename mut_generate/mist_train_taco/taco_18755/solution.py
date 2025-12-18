"""
QUESTION:
One day Bob drew a tree, $\mathbf{T}$, with $n$ nodes and $n-1$ edges on a piece of paper. He soon discovered that parent of a node depends on the root of the tree. The following images shows an example of that:

Learning the fact, Bob invented an exciting new game and decided to play it with Alice. The rules of the game is described below:

Bob picks a random node to be the tree's root and keeps the identity of the chosen node a secret from Alice. Each node has an equal probability of being picked as the root.
Alice then makes a list of $\mathrm{~g~}$ guesses, where each guess is in the form u v and means Alice guesses that $parent(v)=u$ is true. It's guaranteed that an undirected edge connecting $\mbox{u}$ and $\boldsymbol{\nu}$ exists in the tree. 
For each correct guess, Alice earns one point. Alice wins the game if she earns at least $\boldsymbol{\mbox{k}}$ points (i.e., at least $\boldsymbol{\mbox{k}}$ of her guesses were true).

Alice and Bob play $\textit{q}$ games. Given the tree, Alice's guesses, and the value of $\boldsymbol{\mbox{k}}$ for each game, find the probability that Alice will win the game and print it on a new line as a reduced fraction in the format p/q.

Input Format

The first line contains an integer, $\textit{q}$, denoting the number of different games. The subsequent lines describe each game in the following format:

The first line contains an integer, $n$, denoting the number of nodes in the tree.
The $n-1$ subsequent lines contain two space-separated integers, $\mbox{u}$ and $\boldsymbol{\nu}$, defining an undirected edge between nodes $\mbox{u}$ and $\boldsymbol{\nu}$. 
The next line contains two space-separated integers describing the respective values of $\mathrm{~g~}$ (the number of guesses) and $\boldsymbol{\mbox{k}}$ (the minimum score needed to win).
Each of the $\mathrm{~g~}$ subsequent lines contains two space-separated integers, $\mbox{u}$ and $\boldsymbol{\nu}$, indicating Alice guesses $parent(v)=u$.

Constraints

$1\leq q\leq5$
$1\leq n\leq10^5$
$1\leq u,v\leq n$
$1\leq g,k\leq10^5$
The sum of $n$ over all test cases won't exceed $2\times10^5$.
No two guesses will be identical. 

Scoring

For $25\%$ of the maximum score, $1\leq n\leq10^3$.
For $100\%$ of the maximum score, $1\leq n\leq10^5$.

Output Format

Print the probability as a reduced fraction in the format p/q.

Note: Print 0/1 if the probability is $\mbox{0}$ and print 1/1 if the probability is $\mbox{1}$.

Sample Input 0
2
4
1 2
1 3
3 4
2 2
1 2
3 4
3
1 2
1 3
2 2
1 2
1 3

Sample Output 0
1/2
1/3

Explanation 0

Alice and Bob play the following $g=2$ games:

Alice makes two guesses, $\left(1\quad2\right)$ and $\left(3\quad4\right)$ , meaning she guessed that $parent(2)=1$ and $parent(4)=3$. To win the game, at least $k=2$ of her guesses must be true.

In the diagrams below, you can see that at least $2$ guesses are true if the root of the tree is either node $\mbox{1}$ or $3$:

There are $4$ nodes in total and the probability of picking node $\mbox{1}$ or $3$ as the root is $\frac{2}{4}$, which reduces to $\frac{1}{2}$.

In this game, Alice only wins if node $\mbox{1}$ is the root of the tree. There are $3$ nodes in total, and the probability of picking node $\mbox{1}$ as the root is $\frac{1}{3}$.
"""

def calculate_winning_probability(n, edges, guesses, k):
    from math import gcd
    
    # Initialize adjacency list and guess list
    adj = [[] for _ in range(n)]
    p = [[] for _ in range(n)]
    
    # Build the adjacency list
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Build the guess list
    for u, v in guesses:
        p[v].append(u)
    
    # Helper function for DFS to count initial correct guesses
    def dfs(v, par):
        ret = 0
        for u in p[v]:
            ret += 1 if par == u else 0
        for u in adj[v]:
            if u != par:
                ret += dfs(u, v)
        return ret
    
    # Helper function for DFS to count valid root nodes
    def dfs2(v, par, cur, lim):
        if par != -1:
            for u in p[par]:
                if u == v:
                    cur += 1
        for u in p[v]:
            if u == par:
                cur -= 1
        ret = cur >= lim
        for u in adj[v]:
            if u != par:
                ret += dfs2(u, v, cur, lim)
        return ret
    
    # Calculate initial correct guesses
    cur = dfs(0, -1)
    
    # Calculate the number of valid root nodes
    ans = dfs2(0, -1, cur, k)
    
    # Reduce the fraction
    d = gcd(ans, n)
    ans = ans // d
    n = n // d
    
    return (ans, n)