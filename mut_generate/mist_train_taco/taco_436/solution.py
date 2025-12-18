"""
QUESTION:
Given is a tree G with N vertices.
The vertices are numbered 1 through N, and the i-th edge connects Vertex a_i and Vertex b_i.
Consider painting the edges in G with some number of colors.
We want to paint them so that, for each vertex, the colors of the edges incident to that vertex are all different.
Among the colorings satisfying the condition above, construct one that uses the minimum number of colors.

-----Constraints-----
 -  2 \le N \le 10^5
 -  1 \le a_i \lt b_i \le N
 - All values in input are integers.
 - The given graph is a tree.

-----Input-----
Input is given from Standard Input in the following format:
N
a_1 b_1
a_2 b_2
\vdots
a_{N-1} b_{N-1}

-----Output-----
Print N lines.
The first line should contain K, the number of colors used.
The (i+1)-th line (1 \le i \le N-1) should contain c_i, the integer representing the color of the i-th edge, where 1 \le c_i \le K must hold.
If there are multiple colorings with the minimum number of colors that satisfy the condition, printing any of them will be accepted.

-----Sample Input-----
3
1 2
2 3

-----Sample Output-----
2
1
2
"""

def min_color_tree_edges(N, edges):
    # Initialize the adjacency list for the tree
    edge = [[] for _ in range(N)]
    
    # Populate the adjacency list with edges and their indices
    for idx, (a, b) in enumerate(edges):
        edge[a - 1].append((b - 1, idx))
        edge[b - 1].append((a - 1, idx))
    
    # Determine the maximum degree of the tree, which is the minimum number of colors needed
    k = max((len(e) for e in edge))
    
    # Initialize the answer list for edge colors
    ans = [-1] * (N - 1)
    
    # Depth-first search function to color the edges
    def dfs(v=0, p=-1, to_p_col=-1):
        col = 1
        for (u, idx) in edge[v]:
            if u != p:
                if col == to_p_col:
                    col += 1
                ans[idx] = col
                dfs(u, v, col)
                col += 1
    
    # Start the DFS from the root node (vertex 0)
    dfs()
    
    # Return the number of colors used and the list of edge colors
    return k, ans