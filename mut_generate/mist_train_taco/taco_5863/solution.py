"""
QUESTION:
Read problems statements in Mandarin Chinese and Russian as well. 

Alice and Bob are playing the game. Initially, there is a single rooted tree. Players take turns alternately, Alice starts.

In a single turn, Alice should choose any non-empty subset of roots of tree (or trees) and remove them. On the other hand, Bob should choose any non-empty subset of leafs and remove them from the tree (or trees). (Please note that Bob always takes some of the deepest in the original tree leafs.) It's not allowed to skip the turn. The game ends when a player can't take a turn.

The Alice's goal is to minimize the number of turns made by the both players, while Bob wants this number to be the maximal. Considering they both play optimally, what is the number of turns eventually made?

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N denoting the number of nodes of the tree. 

The next N-1 lines contain pairs of nodes' numbers U_{i} and V_{i} (one pair per line), denoting the edges of the tree.

The nodes are numbered from 1 to N, inclusive, and the node with the index 1 is the root of the tree.

------ Output ------ 

For each test case, output a single line containing the answer to the corresponding test case.

------ Constraints ------ 

$1 ≤ T ≤ 40$
$1 ≤ N ≤ 10000$
$1 ≤ U_{i}, V_{i} ≤ N$

------ Example ------ 

Input:
3
2
1 2
7
1 3
1 4
4 2
4 5
4 6
6 7
1

Output:
2
5
1
"""

def calculate_game_turns(T, test_cases):
    results = []
    
    for case in test_cases:
        N, edges = case
        adj = [[] for _ in range(N)]
        
        for u, v in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)
        
        depth_ct = []
        dfs(-1, 0, 0, depth_ct, adj)
        
        max_time = 0
        cum_tot = 0
        for i in range(len(depth_ct) - 1, -1, -1):
            cum_tot += depth_ct[i]
            this_time = min(2 * i + 1, 2 * cum_tot)
            max_time = max(this_time, max_time)
        
        results.append(max_time)
    
    return results

def dfs(parent, n, depth, depth_ct, adj):
    if depth == len(depth_ct):
        depth_ct.append(0)
    depth_ct[depth] += 1
    for c in adj[n]:
        if c != parent:
            dfs(n, c, depth + 1, depth_ct, adj)