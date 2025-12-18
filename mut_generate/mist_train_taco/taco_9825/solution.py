"""
QUESTION:
There are n stones at some integer coordinate points on a 2D plane. Each coordinate point may have at most one stone.
You need to remove some stones. 
A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the maximum possible number of stones that you can remove.
 
Example 1:
Input:
n=6
[[0 0] ,[ 0 1], [1 0] ,[1 2] ,[2 1] ,[2 2]]
Output:
5
Example:
One way to remove 5 stones are
1--[0,0]
2--[1,0]
3--[0,1]
4--[2,1]
5--[1,2]
Your Task:
You don't need to print or input anything. Complete the function maxRemove() which takes an integer array arr, an integer n as the input parameters and returns an integer, denoting the maximum number of stones that can be removed.
 
Expected Time Complexity: O(N+K)
Expected Space Complexity: O(K)
 
Constraints:
1 <= n <=1000
0 <= x[i], y[i]<= 10^{4}
No two stones are at same position.
"""

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def findUParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u, v):
        up_u = self.findUParent(u)
        up_v = self.findUParent(v)
        if up_u == up_v:
            return
        if self.size[up_u] < self.size[up_v]:
            self.parent[up_u] = up_v
            self.size[up_v] += self.size[up_u]
        else:
            self.parent[up_v] = up_u
            self.size[up_u] += self.size[up_v]

def max_remove_stones(stones, n):
    if not stones:
        return 0

    maxr = max(stone[0] for stone in stones)
    maxc = max(stone[1] for stone in stones)
    
    ds = DisjointSet(maxr + 1 + maxc + 1)
    
    for stone in stones:
        row = stone[0]
        col = stone[1] + maxr + 1
        ds.unionBySize(row, col)
    
    bosses = 0
    for i in range(len(ds.parent)):
        if ds.findUParent(i) == i and ds.size[i] > 1:
            bosses += 1
    
    return n - bosses