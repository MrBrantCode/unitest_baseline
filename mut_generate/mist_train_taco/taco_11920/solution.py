"""
QUESTION:
You are given a permutation of the numbers 1, 2, ..., n and m pairs of positions (a_{j}, b_{j}).

At each step you can choose a pair from the given positions and swap the numbers in that positions. What is the lexicographically maximal permutation one can get?

Let p and q be two permutations of the numbers 1, 2, ..., n. p is lexicographically smaller than the q if a number 1 ≤ i ≤ n exists, so p_{k} = q_{k} for 1 ≤ k < i and p_{i} < q_{i}.


-----Input-----

The first line contains two integers n and m (1 ≤ n, m ≤ 10^6) — the length of the permutation p and the number of pairs of positions.

The second line contains n distinct integers p_{i} (1 ≤ p_{i} ≤ n) — the elements of the permutation p.

Each of the last m lines contains two integers (a_{j}, b_{j}) (1 ≤ a_{j}, b_{j} ≤ n) — the pairs of positions to swap. Note that you are given a positions, not the values to swap.


-----Output-----

Print the only line with n distinct integers p'_{i} (1 ≤ p'_{i} ≤ n) — the lexicographically maximal permutation one can get.


-----Example-----
Input
9 6
1 2 3 4 5 6 7 8 9
1 4
4 7
2 5
5 8
3 6
6 9

Output
7 8 9 4 5 6 1 2 3
"""

def get_lexicographically_maximal_permutation(n, m, permutation, pairs):
    adj = [[] for _ in range(n)]
    
    # Build the adjacency list
    for (u, v) in pairs:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    
    visited = [0] * n
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        num = [permutation[i]]
        i_list = [i]
        stack = [i]
        
        # Perform DFS to find connected components
        while stack:
            v = stack.pop()
            for dest in adj[v]:
                if not visited[dest]:
                    visited[dest] = 1
                    num.append(permutation[dest])
                    i_list.append(dest)
                    stack.append(dest)
        
        # Sort the numbers in descending order and assign them back to the positions
        num.sort(reverse=True)
        i_list.sort()
        for (j, v) in zip(i_list, num):
            permutation[j] = v
    
    return permutation