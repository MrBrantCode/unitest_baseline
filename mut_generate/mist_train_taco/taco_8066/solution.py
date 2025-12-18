"""
QUESTION:
You are given a tree with N nodes with every node being colored. A color is represented by an integer ranging from 1 to 10^{9}. Can you find the number of distinct colors available in a subtree rooted at the node s? 

Input Format 

The first line contains three space separated integers representing the number of nodes in the tree (N), number of queries to answer (M) and the root of the tree. 

In each of the next N-1 lines, there are two space separated integers(a b) representing an edge from node a to Node b and vice-versa.   

N lines follow: N+$i^{th} $line contains the color of the$ i^{th} $node.

M lines follow: Each line containg a single integer s.

Output Format 

Output exactly M lines, each line containing the output of the i_{th} query.

Constraints 

0 <= M <= $10^{5}$

1 <= N <= $10^{5}$

1 <= root <= N

1 <= color of the Node <=$ 10^{9}$

Example

Sample Input

4 2 1
1 2
2 4
2 3
10
20
20
30
1
2

Sample Output

3
2

Explanation

Query 1-Subtree rooted at 1 is the entire tree and colors used are 10 20 20 30 , so the answer is 3(10,20 and 30)

Query 2-Subtree rooted at 2 contains color 20 20 30, so the answer is 2(20 and 30)
"""

def count_distinct_colors_in_subtree(n, edges, colors, queries):
    from collections import defaultdict
    
    class Node:
        def __init__(self, label, color):
            self.label = label
            self.color = color
            self.children = []
            self.parent = None
            self.distinct_colors = set()
    
    # Build the tree
    nodes = {i: Node(i, colors[i-1]) for i in range(1, n+1)}
    for (u, v) in edges:
        nodes[u].children.append(nodes[v])
        nodes[v].children.append(nodes[u])
    
    # Set the root and calculate distinct colors in subtrees
    def dfs(node, parent):
        node.parent = parent
        node.distinct_colors.add(node.color)
        for child in node.children:
            if child != parent:
                dfs(child, node)
                node.distinct_colors.update(child.distinct_colors)
    
    dfs(nodes[1], None)  # Assuming the root is always node 1
    
    # Answer the queries
    results = []
    for query in queries:
        results.append(len(nodes[query].distinct_colors))
    
    return results