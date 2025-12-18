"""
QUESTION:
You are given a tree that is built in a following way: initially there is single vertex 1. All the other vertices are added one by one, from vertex 2 to vertex N, by connecting it to one of those that have been added before. You are to find the diameter of the tree after adding each vertex. Let the distance between vertex u and v be the minimal number of edges you have to pass to get from u to v, then diameter is the maximum distance between any two pairs (u,v) that have already been added to the tree.

------ Input ------ 

The input consists of several Test cases. The file line of input contains an integer T, the number of test cases. T test cases follow.
The first line of each test case contains an integer N, then N-1 lines follow: ith line contains an integer P_{i}, which means that vertex i+1 is connected to the vertex P_{i}. 

------ Output ------ 

For each test case, output N-1 lines - the diameter after adding vertices 2, 3,..,N

------ Constraints ------ 

1 ≤ T ≤ 15
1 ≤ N ≤ 10^{5}
P_{i} ≤ i 
Sum of N over all test cases in a file does not exceed 2 * 10^{5}

------ Example ------ 

Input:
2
3
1
1
5
1
2
3
3

Output:
1
2
1
2
3
3
"""

def calculate_tree_diameters(test_cases):
    def update(M, level, u, v):
        level[u] = level[v] + 1
        M[u][0] = v
        for j in range(1, 18):
            if M[u][j - 1]:
                M[u][j] = M[M[u][j - 1]][j - 1]

    def LCA(M, level, u, v):
        if u == v:
            return u
        if level[u] < level[v]:
            (u, v) = (v, u)
        for i in range(17, -1, -1):
            if M[u][i] and level[M[u][i]] >= level[v]:
                u = M[u][i]
        if u == v:
            return u
        for i in range(17, -1, -1):
            if M[u][i] and M[u][i] != M[v][i]:
                u = M[u][i]
                v = M[v][i]
        return M[u][0]

    def distance(M, level, a, b):
        return level[a] + level[b] - 2 * level[LCA(M, level, a, b)]

    results = []

    for test_case in test_cases:
        N = len(test_case) + 1
        M = [[0 for _ in range(18)] for _ in range(N + 5)]
        level = [0] * N
        (u, v) = (0, 0)
        test_results = []
        diameter = 0

        for i in range(1, N):
            p = test_case[i - 1]
            update(M, level, i, p - 1)
            cur = distance(M, level, i, u)
            if cur > diameter:
                diameter = cur
                v = i
            else:
                cur = distance(M, level, i, v)
                if cur > diameter:
                    diameter = cur
                    u = i
            test_results.append(diameter)

        results.append(test_results)

    return results