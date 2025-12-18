"""
QUESTION:
When Darth Vader gets bored, he sits down on the sofa, closes his eyes and thinks of an infinite rooted tree where each node has exactly n sons, at that for each node, the distance between it an its i-th left child equals to d_{i}. The Sith Lord loves counting the number of nodes in the tree that are at a distance at most x from the root. The distance is the sum of the lengths of edges on the path between nodes.

But he has got used to this activity and even grew bored of it. 'Why does he do that, then?' — you may ask. It's just that he feels superior knowing that only he can solve this problem. 

Do you want to challenge Darth Vader himself? Count the required number of nodes. As the answer can be rather large, find it modulo 10^9 + 7.


-----Input-----

The first line contains two space-separated integers n and x (1 ≤ n ≤ 10^5, 0 ≤ x ≤ 10^9) — the number of children of each node and the distance from the root within the range of which you need to count the nodes.

The next line contains n space-separated integers d_{i} (1 ≤ d_{i} ≤ 100) — the length of the edge that connects each node with its i-th child.


-----Output-----

Print a single number — the number of vertexes in the tree at distance from the root equal to at most x. 


-----Examples-----
Input
3 3
1 2 3

Output
8



-----Note-----

Pictures to the sample (the yellow color marks the nodes the distance to which is at most three) [Image]
"""

def count_nodes_within_distance(n, x, d):
    MOD = 1000000007
    N = 101

    def mul_vec_mat(v, a):
        n = len(a[0])
        m = len(v)
        c = [0] * n
        for i in range(n):
            c[i] = sum((a[j][i] * v[j] % MOD for j in range(m))) % MOD
        return c

    def mul_vec_sparse_mat(v, ta):
        n = len(ta)
        c = [0] * n
        for i in range(n):
            c[i] = sum((x * v[j] % MOD for (j, x) in ta[i])) % MOD
        return c

    def mod_pow_kitamasa(a, x):
        n = len(a)
        ta = [[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if a[i][j] != 0:
                    ta[j].append((i, a[i][j]))
        r = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        while x > 0:
            if x & 1:
                r[1] = mul_vec_mat(r[1], a)
            aa = [[0] * n for i in range(n)]
            aa[0] = a[0]
            aa[1] = mul_vec_mat(a[1], a)
            for i in range(2, n):
                aa[i] = mul_vec_sparse_mat(aa[i - 1], ta)
            a = aa
            x >>= 1
        for i in range(2, n):
            r[i] = mul_vec_sparse_mat(r[i - 1], ta)
        return r

    a = [[0] * N for i in range(N)]
    a[0][0] = 1
    a[N - 1][0] = 1
    for i in range(1, N - 1):
        a[i][i + 1] = 1
    for di in d:
        a[N - 1][N - di] += 1

    a = mod_pow_kitamasa(a, x)
    b = [0] * N
    b[0] = 1
    b[N - 1] = 1

    return sum((a[N - 1][i] * b[i] % MOD for i in range(N))) % MOD