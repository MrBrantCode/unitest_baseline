"""
QUESTION:
Given a 2D matrix g contains only 1 and 0, count the number of triangles in it.
Take 3 index i,j,k (0<=i,j,k<n). {i,j}, {j,k}, {k,i} will form a triangle if i!=j and i!=k and j!=k and g[i][j]=1 and g[j][k]=1 and g[k][i]=1.
Example 1:
Input:
N=4
graph[][]={{0, 0, 1, 0}, 
           {1, 0, 0, 1},
           {0, 1, 0, 0}, 
           {0, 0, 1, 0}}
Output:
2
Explanation;
Triangle 1: {{0,2}, {2,1}, {1,0}}
graph[][]={{0, 0, 1, 0},
           {1, 0, 0, 1},
           {0, 1, 0, 0},
           {0, 0, 1, 0}}.  
Triangle 2: {{1,3}, {3,2}, {2,1}}
graph[][]={{0, 0, 1, 0},
           {1, 0, 0, 1},
           {0, 1, 0, 0},
           {0, 0, 1, 0}}. 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function numberOfTriangles() which takes the 2D matrix g[][], it's number of nodes N as input parameters and returns the number of triangles in it.
 
Expected Time Complexity: O(N*N*N)
Expected Auxiliary Space: O(1)
 
Constraints:
1<=N<=100
0<=g[i][j]<=1
"""

from typing import List

def count_triangles(n: int, g: List[List[int]]) -> int:
    cnt = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k and g[i][j] == 1 and g[j][k] == 1 and g[k][i] == 1:
                    cnt += 1
    return cnt // 3