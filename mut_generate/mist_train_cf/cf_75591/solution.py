"""
QUESTION:
Given a tree with n nodes, where each node has a label represented by a lower-case character, and edges connecting the nodes, return an array of size n where each element at index i represents the number of nodes in the subtree of the ith node that have the same label as node i and are at most d distance away from node i.

The tree is defined by the number of nodes n, the edges array representing the connections between nodes, the labels string representing the labels of each node, and the distance d. The function to be implemented is `countSubTrees(n, edges, labels, d)`. 

Constraints: 
1 <= n <= 10^5 
edges.length == n - 1 
edges[i].length == 2 
0 <= ai, bi < n 
ai != bi 
labels.length == n 
labels consists of only lower-case English letters. 
1 <= d <= n
"""

from collections import defaultdict
from string import ascii_lowercase

def countSubTrees(n, edges, labels, d):
    """
    This function returns an array of size n where each element at index i represents 
    the number of nodes in the subtree of the ith node that have the same label as 
    node i and are at most d distance away from node i.

    Parameters:
    n (int): The number of nodes in the tree.
    edges (list): A list of edges in the tree where each edge is represented as a list of two nodes.
    labels (str): A string representing the labels of each node in the tree.
    d (int): The maximum distance from each node.

    Returns:
    list: An array of size n where each element at index i represents the number of 
    nodes in the subtree of the ith node that have the same label as node i and are 
    at most d distance away from node i.
    """
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    res = [0] * n
    visited = [0] * n

    def dfs(node):
        visited[node] = 1
        count = dict((c, 0) for c in ascii_lowercase)
        count[labels[node]] += 1
        for child in graph[node]:
            if visited[child] == 0:
                nextCount = dfs(child)
                for c in ascii_lowercase:
                    if (count[c] + nextCount[c]) <= d:
                        count[c] += nextCount[c]
        res[node] = count[labels[node]]
        return count

    dfs(0)
    return res