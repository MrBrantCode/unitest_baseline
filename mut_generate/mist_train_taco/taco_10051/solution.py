"""
QUESTION:
Emuskald considers himself a master of flow algorithms. Now he has completed his most ingenious program yet — it calculates the maximum flow in an undirected graph. The graph consists of n vertices and m edges. Vertices are numbered from 1 to n. Vertices 1 and n being the source and the sink respectively.

However, his max-flow algorithm seems to have a little flaw — it only finds the flow volume for each edge, but not its direction. Help him find for each edge the direction of the flow through this edges. Note, that the resulting flow should be correct maximum flow.

More formally. You are given an undirected graph. For each it's undirected edge (ai, bi) you are given the flow volume ci. You should direct all edges in such way that the following conditions hold:

  1. for each vertex v (1 < v < n), sum of ci of incoming edges is equal to the sum of ci of outcoming edges; 
  2. vertex with number 1 has no incoming edges; 
  3. the obtained directed graph does not have cycles. 

Input

The first line of input contains two space-separated integers n and m (2 ≤ n ≤ 2·105, n - 1 ≤ m ≤ 2·105), the number of vertices and edges in the graph. The following m lines contain three space-separated integers ai, bi and ci (1 ≤ ai, bi ≤ n, ai ≠ bi, 1 ≤ ci ≤ 104), which means that there is an undirected edge from ai to bi with flow volume ci.

It is guaranteed that there are no two edges connecting the same vertices; the given graph is connected; a solution always exists.

Output

Output m lines, each containing one integer di, which should be 0 if the direction of the i-th edge is ai → bi (the flow goes from vertex ai to vertex bi) and should be 1 otherwise. The edges are numbered from 1 to m in the order they are given in the input.

If there are several solutions you can print any of them.

Examples

Input

3 3
3 2 10
1 2 10
3 1 5


Output

1
0
1


Input

4 5
1 2 10
1 3 10
2 3 5
4 2 15
3 4 5


Output

0
0
1
1
0

Note

In the first test case, 10 flow units pass through path <image>, and 5 flow units pass directly from source to sink: <image>.
"""

from collections import deque

def determine_edge_directions(n, m, edges):
    DST_VERTEX = 0
    EDGE_CAP = 1
    EDGE_ID = 2
    EDGE_DIR = 3

    def bfs(flow, graph, n, m):
        dirs = [-1 for _ in range(m)]
        q = deque()
        q.append(0)
        q_size = 1
        while q_size > 0:
            cur_node = q.popleft()
            q_size -= 1
            for i in range(len(graph[cur_node])):
                cur_id = graph[cur_node][i][EDGE_ID]
                if dirs[cur_id] == -1:
                    dirs[cur_id] = graph[cur_node][i][EDGE_DIR]
                    cur_dst = graph[cur_node][i][DST_VERTEX]
                    flow[cur_dst] -= graph[cur_node][i][EDGE_CAP]
                    if cur_dst != n - 1 and flow[cur_dst] == 0:
                        q.append(cur_dst)
                        q_size += 1
        return dirs

    flow = [0 for _ in range(n)]
    graph = [[] for _ in range(n)]
    
    for j, (src, dst, cap) in enumerate(edges):
        src -= 1
        dst -= 1
        graph[src].append((dst, cap, j, 0))
        graph[dst].append((src, cap, j, 1))
        flow[src] += cap
        flow[dst] += cap
    
    for i in range(n):
        flow[i] //= 2
    
    dirs = bfs(flow, graph, n, m)
    return dirs