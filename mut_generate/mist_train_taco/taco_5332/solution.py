"""
QUESTION:
Example

Input

3
0 2 7
2 0 4
5 8 0


Output

11
"""

def calculate_minimum_edge_sum(n, edges):
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            ans += min(edges[i][j], edges[j][i])
    return ans