"""
QUESTION:
You are given a n,m which means the row and column of the 2D matrix and an array of  size k denoting the number of operations. Matrix elements is 0 if there is water or 1 if there is land. Originally, the 2D matrix is all 0 which means there is no land in the matrix. The array has k operator(s) and each operator has two integer A[i][0], A[i][1] means that you can change the cell matrix[A[i][0]][A[i][1]] from sea to island. Return how many island are there in the matrix after each operation.You need to return an array of size k.
Note : An island means group of 1s such that they share a common side.
 
Example 1:
Input: n = 4
m = 5
k = 4
A = {{1,1},{0,1},{3,3},{3,4}}
Output: 1 1 2 2
Explanation:
0.  00000
    00000
    00000
    00000
1.  00000
    01000
    00000
    00000
2.  01000
    01000
    00000
    00000
3.  01000
    01000
    00000
    00010
4.  01000
    01000
    00000
    00011
 
 
Example 2:
Input: n = 4
m = 5
k = 4
A = {{0,0},{1,1},{2,2},{3,3}}
Output: 1 2 3 4
Explanation:
0.  00000
    00000
    00000
    00000
1.  10000
    00000
    00000
    00000
2.  10000
    01000
    00000
    00000
3.  10000
    01000
    00100
    00000
4.  10000
    01000
    00100
    00010
 
Your Task:
You don't need to read or print anything. Your task is to complete the function numOfIslands() which takes an integer n denoting no. of rows in the matrix, an integer m denoting the number of columns in the matrix and a 2D array of size k denoting  the number of operators.
Expected Time Complexity: O(m * n)
Expected Auxiliary Space: O(m * n)
Constraints:
1 <= n,m <= 100
1 <= k <= 1000
"""

from typing import List

def findPar(node, parent):
    if node == parent[node]:
        return node
    parent[node] = findPar(parent[node], parent)
    return parent[node]

def union(u, v, rank, parent):
    (ult_u, ult_v) = (findPar(u, parent), findPar(v, parent))
    if ult_u == ult_v:
        return True
    if rank[ult_u] < rank[ult_v]:
        parent[ult_u] = ult_v
    elif rank[ult_v] < rank[ult_u]:
        parent[ult_v] = ult_u
    else:
        parent[ult_v] = ult_u
        rank[ult_u] += 1
    return False

def num_of_islands(rows: int, cols: int, operators: List[List[int]]) -> List[int]:
    rank = [0] * (rows * cols)
    parent = [i for i in range(rows * cols)]
    vis = [[0 for _ in range(cols)] for _ in range(rows)]
    dirc = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    res = []
    cnt = 0
    
    for pair in operators:
        r, c = pair
        if vis[r][c] == 1:
            res.append(cnt)
            continue
        
        vis[r][c] = 1
        cnt += 1
        u = r * cols + c
        
        for i in dirc:
            x, y = r + i[0], c + i[1]
            if x < 0 or y < 0 or x >= rows or y >= cols:
                continue
            if vis[x][y] == 1:
                v = x * cols + y
                if not union(u, v, rank, parent):
                    cnt -= 1
        
        res.append(cnt)
    
    return res