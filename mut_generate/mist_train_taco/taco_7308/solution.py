"""
QUESTION:
You are given a string s of length n.
Does a tree with n vertices that satisfies the following conditions exist?
 - The vertices are numbered 1,2,..., n.
 - The edges are numbered 1,2,..., n-1, and Edge i connects Vertex u_i and v_i.
 - If the i-th character in s is 1, we can have a connected component of size i by removing one edge from the tree.
 - If the i-th character in s is 0, we cannot have a connected component of size i by removing any one edge from the tree.
If such a tree exists, construct one such tree.

-----Constraints-----
 - 2 \leq n \leq 10^5
 - s is a string of length n consisting of 0 and 1.

-----Input-----
Input is given from Standard Input in the following format:
s

-----Output-----
If a tree with n vertices that satisfies the conditions does not exist, print -1.
If a tree with n vertices that satisfies the conditions exist, print n-1 lines.
The i-th line should contain u_i and v_i with a space in between.
If there are multiple trees that satisfy the conditions, any such tree will be accepted.

-----Sample Input-----
1111

-----Sample Output-----
-1

It is impossible to have a connected component of size n after removing one edge from a tree with n vertices.
"""

def construct_tree_from_string(s: str) -> list[tuple[int, int]] | int:
    n = len(s)
    
    # Check for invalid conditions
    if s[0] == '0' or s[-1] == '1':
        return -1
    
    # Check symmetry condition
    for i in range(n // 2):
        if s[i] != s[n - 2 - i]:
            return -1
    
    # Construct the tree
    edges = []
    for i in range(2, n // 2 + 1):
        edges.append((1, i))
    
    bef = 1
    for i in range(n // 2 + 1, n + 1):
        edges.append((bef, i))
        if s[i - 2] == '1':
            bef = i
    
    return edges