"""
QUESTION:
Implement the function `maxCountNodes(tree, costs, budget)` to calculate the maximum number of nodes that can be monitored within a given budget by installing cameras on the nodes of the binary tree. The tree is represented as an adjacency list where each index `i` in the list represents a node and its value at index `i` is the index of its parent node, and the costs of cameras are given in the `costs` array. The function should return the maximum number of nodes that can be monitored with the given budget. 

Restrictions: The number of nodes in the tree will be in the range `[1, 1000]`. Every node has value 0. The cost of each camera will be in the range `[1, 100]`. The budget will be in the range `[1, 10000]`.
"""

from collections import defaultdict

def maxCountNodes(tree, costs, budget):
    dp = defaultdict(lambda: [-1, -1]) # DP Table
    edges = defaultdict(list) # adjacency list representation of the tree

    for u, v in tree[:-1]: # constructing the tree
        edges[u].append(v)
        edges[v].append(u)

    def dfs(node, parent):
        if dp[node][0] != -1: # if the result is already computed
            return dp[node]

        # Calculating the maximum nodes assuming we installed a camera at this node
        withCamera = costs[node]
        for child in edges[node]:
            if child == parent:
                continue
            withCamera += dfs(child, node)[1]

        # Considering the case where we do not place a camera at the node
        withoutCamera = 0
        for child in edges[node]:
            if child == parent:
                continue
            withoutCamera += max(dfs(child, node))

        # Check if we have enough budget to place a camera at the node
        if withCamera <= budget:
            dp[node][0] = max(dp[node][0], withCamera, withoutCamera)
        else:
            dp[node][0] = withoutCamera

        dp[node][1] = withoutCamera # maximum nodes without camera on node

        return dp[node]

    maxCount = max(dfs(0, -1)) # start dfs traversal from root node
    return maxCount