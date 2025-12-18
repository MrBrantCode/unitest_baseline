"""
QUESTION:
Roughly speaking, this problem asks you to create the checker of [*the problem used in December CookOff*].

You are given a tree with N vertices and a string C of length N, consisting of the characters 'R', 'G' and 'B'.

For each integer i\ (1≤ i≤ N), C_{i} is the color of vertex i — 'R' is for Red, 'G' is for Green and 'B' is for Blue.

The input is called valid if for all pairs of Blue vertices (u,\ v),\ u\neq v, there is at least one Red vertex and one Green vertex on the [simple path] between u and v.

Your task is to validate the input for given T test cases. For each test case, print Yes if the input is valid, otherwise No.

------ Input Format ------ 

- The first line of input contains one positive integer T, the number of test cases. The description of T test cases follows.
- The first line of each test case contains one positive integer N, the number of vertices of the tree.
- The second line of each test case contains a string C, denoting the colors of the vertices.
- Each of the following N - 1 lines contains two space-separated integers u and v, denoting an edge between vertices u and v in the tree.

------ Output Format ------ 

For each test case, output a single line containing Yes if the input is valid, and No otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

------ Constraints ------ 

$1 ≤ T ≤ 10^{4} $
$1 ≤ N ≤ 2\cdot 10^{5}$
- The sum of $N$ for each test case is at most $2\cdot 10^{5}$
$|C|=N$
$C$ consists of three types of characters, 'R', 'G' and 'B'
$1 ≤ u, v ≤ N, u \neq v$
- The input graph forms a tree

----- Sample Input 1 ------ 
5
4
BRGB
3 2
1 2
4 3
3
RGB
1 2
2 3
1
B
2
BB
1 2
4
BRGB
3 2
1 2
4 2
----- Sample Output 1 ------ 
Yes
Yes
Yes
No
No
----- explanation 1 ------ 
- Test case 1:
- The only pair is $(1, 4)$.
- Test case 3:
- There are no pairs.
- Test case 5:
- The only pair is $(1, 4)$. There are no Green vertices on the path between $1$ and $4$.
"""

def validate_tree_colors(T, test_cases):
    results = []
    
    for case in test_cases:
        N, C, edges = case
        graph = [[] for _ in range(N + 1)]
        
        for u, v in edges:
            if C[u - 1] == 'R' and C[v - 1] == 'G' or (C[u - 1] == 'G' and C[v - 1] == 'R'):
                continue
            graph[u].append(v)
            graph[v].append(u)
        
        visit = set()
        
        def dfs(u, count):
            visit.add(u)
            if C[u - 1] == 'B':
                count[0] += 1
            if count[0] > 1:
                return False
            for v in graph[u]:
                if v not in visit:
                    if not dfs(v, count):
                        return False
            return True
        
        flag = False
        for i in range(1, N + 1):
            if i not in visit:
                if not dfs(i, [0]):
                    flag = True
                    break
        
        if flag:
            results.append('No')
        else:
            results.append('Yes')
    
    return results