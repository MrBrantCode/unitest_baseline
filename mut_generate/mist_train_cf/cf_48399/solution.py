"""
QUESTION:
Generate a list of all possible full binary trees with `N` nodes, where each node has `Node.val == 0` and each node has either `0` or `2` children. The order of the final list of trees does not matter. The function should be named `allPossibleFBT(N)`, where `1 <= N <= 20` and `N` is an odd integer.
"""

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def allPossibleFBT(N):
    dp = [[] for _ in range(21)]
    dp[1].append(Node(0))

    for i in range(2, N+1):
        if i % 2 == 1:  # only possible when N is odd
            for j in range(1, i, 2):
                lefts = dp[j]  # all possibilities for left subtree
                rights = dp[i-j-1]  # all possibilities for right subtree
                for left in lefts:
                    for right in rights:
                        root = Node(0)
                        root.left = left
                        root.right = right
                        dp[i].append(root)
    return dp[N]