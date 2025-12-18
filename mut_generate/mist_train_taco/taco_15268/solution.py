"""
QUESTION:
Russian Translation Available

You have a graph with N vertices and M edges. Someone has chosen N-1 edges of these M and claims that they form a spanning tree. Just check whether it's true or not.

Input

The first line contains one integer T denoting the number of test cases.
Each test case starts with a line containing 2 space-separated integers: N and M. Each of the following M lines contains description of one edge: two different space-separated integers a and b from 1 to N each - numbers of vertices that are connected by this edge. The last line of each test case contains N - 1 space-separated integers - numbers of chosen edges. Edges are enumerated from 1 in the input order.

Output

For each test case output either YES if the chosen N-1 edges form a spanning tree  or NO otherwise.

Constrains
1 ≤ T ≤ 20
1 ≤ N ≤ 5000
1 ≤ M ≤ 40 000

SAMPLE INPUT
2
4 4
1 2
1 3
2 3
1 4
1 2 3
4 4
1 2
1 3
2 3
1 4
2 3 4


SAMPLE OUTPUT
NO
YES
"""

def is_spanning_tree(test_cases):
    results = []
    
    for case in test_cases:
        N = case['N']
        M = case['M']
        edges = case['edges']
        chosen_edges = case['chosen_edges']
        
        flag = [False] * (N + 1)
        
        for edge_index in chosen_edges:
            edge = edges[edge_index - 1]
            flag[edge[0]] = True
            flag[edge[1]] = True
        
        spanning_tree = all(flag[1:])
        
        if spanning_tree:
            results.append("YES")
        else:
            results.append("NO")
    
    return results