"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

While vacationing in Egypt, Chef found a recipe of an ancient dish. The receipt is a sequence of hieroglyphs written on a magic paper - it survived for thousands of years! The sequence is written on a long scroll. Unfortunately, the scroll is split into pieces, and possibly, some pieces of the scroll are missing. Chef has a total of N pieces, numbered for convenience from 1 to N. He gave the pieces of a tape to his friend who studies hieroglyphs for analysis. Chef was happy to hear that there are some relations between the pieces. Some of the pieces may follow other pieces.
The informations about these relations is given as a list of M pairs (A_{i}, B_{i}). Such a pair means that the A_{i}^{th} piece can be immediately followed by the B_{i}^{th} one.
Chef is working on recovering the recipe to prepare this dish for his Egyptian friends. He wants to place all the pieces into lines such that any pair of consecutive pieces (L, R) in a line must be explicitly allowed by one of the M rules described above. In other words, for some i (1 ≤ i ≤ M), (A_{i}, B_{i}) = (L, R). It appears that in general, not all the pieces can be placed in a single line while following the rules. So, please help Chef find what is the minimum number of lines required for all the pieces to be placed acoording to the rules.

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and M denoting the number of pieces and number of relations of those N pieces. Next M lines contain two space-separated integers A and B denoting that piece number A can be followed by piece number B, all those pairs are guaraneed to be unique within a test case.

------ Output ------ 

For each test case, output a single line containing the minimum number of lines required for all the pieces to be placed acoording to the rules.

------ Constraints ------ 

$1 ≤ T ≤ 20$
$1 ≤ N ≤ 100$
$1 ≤ M ≤ N^{2}$
$1 ≤ A_{i} ≤ N$
$1 ≤ B_{i} ≤ N$
$There is no sequence S_{1}, S_{2}, ..., S_{k} such that the piece S_{i} can be immediately followed by the piece S_{i+1} for all i from 1 to k-1, and that piece S_{k} can be followed by piece S_{1}.$

----- Sample Input 1 ------ 
3

3 3

1 2

2 3

1 3

3 2

1 2

1 3

5 4

1 3

2 3

3 4

2 5
----- Sample Output 1 ------ 
1

2

2
"""

def minimum_lines_for_recipe(T, test_cases):
    results = []
    for case in test_cases:
        N, M, relations = case
        s, t = 0, 2 * N + 1
        res = [[0] * (t + 1) for _ in range(t + 1)]
        
        for i in range(N):
            res[s][i + 1], res[i + 1 + N][t] = 1, 1
        
        for A, B in relations:
            if A != B:
                res[A][B + N] = 1
        
        max_flow = dinic(res)
        results.append(N - max_flow)
    
    return results

def augment(res, u, t, level, limit):
    if limit == 0:
        return 0
    if u == t:
        return limit
    flow = 0
    for v in range(len(res)):
        if res[u][v] > 0 and level[v] == level[u] + 1:
            aug = augment(res, v, t, level, min(limit, res[u][v]))
            res[u][v] -= aug
            res[v][u] += aug
            flow += aug
            limit -= aug
    if not flow:
        level[u] = None
    return flow

def dinic(res):
    from collections import deque
    q = deque()
    max_flow = 0
    s, t = 0, len(res) - 1
    while True:
        q.append(s)
        level = [None] * len(res)
        level[s] = 0
        while q:
            u = q.popleft()
            for v in range(len(res)):
                if res[u][v] > 0 and level[v] is None:
                    level[v] = level[u] + 1
                    q.append(v)
        if level[t] is None:
            return max_flow
        max_flow += augment(res, s, t, level, sum(res[s][v] for v in range(len(res))))