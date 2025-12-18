"""
QUESTION:
Iahub is very proud of his recent discovery, propagating trees. Right now, he invented a new tree, called xor-tree. After this new revolutionary discovery, he invented a game for kids which uses xor-trees.

The game is played on a tree having n nodes, numbered from 1 to n. Each node i has an initial value initi, which is either 0 or 1. The root of the tree is node 1.

One can perform several (possibly, zero) operations on the tree during the game. The only available type of operation is to pick a node x. Right after someone has picked node x, the value of node x flips, the values of sons of x remain the same, the values of sons of sons of x flips, the values of sons of sons of sons of x remain the same and so on.

The goal of the game is to get each node i to have value goali, which can also be only 0 or 1. You need to reach the goal of the game by using minimum number of operations.

Input

The first line contains an integer n (1 ≤ n ≤ 105). Each of the next n - 1 lines contains two integers ui and vi (1 ≤ ui, vi ≤ n; ui ≠ vi) meaning there is an edge between nodes ui and vi. 

The next line contains n integer numbers, the i-th of them corresponds to initi (initi is either 0 or 1). The following line also contains n integer numbers, the i-th number corresponds to goali (goali is either 0 or 1).

Output

In the first line output an integer number cnt, representing the minimal number of operations you perform. Each of the next cnt lines should contain an integer xi, representing that you pick a node xi.

Examples

Input

10
2 1
3 1
4 2
5 1
6 2
7 5
8 6
9 8
10 5
1 0 1 1 0 1 0 1 0 1
1 0 1 0 0 1 1 1 0 1


Output

2
4
7
"""

def min_operations_to_reach_goal(n, edges, initial_values, goal_values):
    N = 100003  # A constant to ensure adjacency list size is sufficient
    adj = [[] for _ in range(N)]
    
    # Build the adjacency list
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Initial and goal values with a dummy element at the start
    a = [0] + initial_values
    b = [0] + goal_values
    
    # Calculate the difference array
    d = [i ^ j for i, j in zip(a, b)]
    
    res = []
    
    def dfs(u, p, c_lvl, p_lvl):
        stk = [(u, p, c_lvl, p_lvl)]
        while stk:
            u, p, c_lvl, p_lvl = stk.pop()
            if c_lvl != d[u]:
                c_lvl = 1 - c_lvl
                res.append(u)
            for v in adj[u]:
                if v != p:
                    stk.append((v, u, p_lvl, c_lvl))
    
    # Start DFS from the root node (node 1)
    dfs(1, 0, 0, 0)
    
    # Return the result
    cnt = len(res)
    operations = res
    return cnt, operations