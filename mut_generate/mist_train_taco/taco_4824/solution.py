"""
QUESTION:
You are given a functional graph. It is a directed graph, in which from each vertex goes exactly one arc. The vertices are numerated from 0 to n - 1.

Graph is given as the array f_0, f_1, ..., f_{n} - 1, where f_{i} — the number of vertex to which goes the only arc from the vertex i. Besides you are given array with weights of the arcs w_0, w_1, ..., w_{n} - 1, where w_{i} — the arc weight from i to f_{i}. [Image] The graph from the first sample test. 

Also you are given the integer k (the length of the path) and you need to find for each vertex two numbers s_{i} and m_{i}, where:  s_{i} — the sum of the weights of all arcs of the path with length equals to k which starts from the vertex i;  m_{i} — the minimal weight from all arcs on the path with length k which starts from the vertex i. 

The length of the path is the number of arcs on this path.


-----Input-----

The first line contains two integers n, k (1 ≤ n ≤ 10^5, 1 ≤ k ≤ 10^10). The second line contains the sequence f_0, f_1, ..., f_{n} - 1 (0 ≤ f_{i} < n) and the third — the sequence w_0, w_1, ..., w_{n} - 1 (0 ≤ w_{i} ≤ 10^8).


-----Output-----

Print n lines, the pair of integers s_{i}, m_{i} in each line.


-----Examples-----
Input
7 3
1 2 3 4 3 2 6
6 3 1 4 2 2 3

Output
10 1
8 1
7 1
10 2
8 2
7 1
9 3

Input
4 4
0 1 2 3
0 1 2 3

Output
0 0
4 1
8 2
12 3

Input
5 3
1 2 3 4 0
4 1 2 14 3

Output
7 1
17 1
19 2
21 3
8 1
"""

def calculate_path_weights(n, k, f, w):
    max_log = 35
    next_n = [[-1] * n for _ in range(max_log)]
    next_m = [[float('inf')] * n for _ in range(max_log)]
    next_s = [[0] * n for _ in range(max_log)]
    
    for u in range(n):
        v = f[u]
        next_n[0][u] = v
        next_m[0][u] = w[u]
        next_s[0][u] = w[u]
    
    for k_log in range(1, max_log):
        for u in range(n):
            v = next_n[k_log - 1][u]
            m = next_m[k_log - 1][u]
            s = next_s[k_log - 1][u]
            next_n[k_log][u] = next_n[k_log - 1][v]
            next_m[k_log][u] = min(next_m[k_log - 1][v], m)
            next_s[k_log][u] = next_s[k_log - 1][v] + s
    
    result = []
    for u in range(n):
        s, m = 0, float('inf')
        v = u
        cur = 1 << max_log
        i = max_log
        while cur > 0:
            if cur & k:
                m = min(m, next_m[i][v])
                s = s + next_s[i][v]
                v = next_n[i][v]
            cur >>= 1
            i -= 1
        result.append((s, m))
    
    return result