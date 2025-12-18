"""
QUESTION:
You have given N cities numbered from 0 to N-1. The distance between each pair of cities is given by N * N matrix MAT where MAT[i][j] denotes the distance between city i and j.
The task is to select K (K<= N) ATM servers  in such a way that the maximum distance of a city from the ATM Server is minimized.
Example 1:
Input: N = 4, K = 2,
MAT[][] = {{0, 10, 7, 6},
           {10, 0, 8, 5},
           {7, 8, 0, 12},
           {6, 5, 12, 0}}
Output: 6
Explanation:
Your Task:
You don't need to read or print anything. Your task is to complete the function selectKcities() which takes N, K  and MAT[][] as input parameter and returns an integer, indicating the maximum distance of a city from the ATM Server, which is minimized.
Expected Time Complexity: O(N * K * (2 ^ N))
Expected Space Complexity: O(K)
 
Constraints:
1 <= K <= N <= 15
1 <= MAT[i][j] <= 10^9
"""

from typing import List

def select_k_cities(n: int, k: int, mat: List[List[int]]) -> int:
    def solve(mat, n, u, dist, kAtms):
        if kAtms == 0 or u == n:
            return max(dist)
        temp = []
        for v, val in enumerate(dist):
            temp.append(min(val, mat[u][v]))
        c1 = solve(mat, n, u + 1, temp, kAtms - 1)
        c2 = solve(mat, n, u + 1, dist, kAtms)
        return min(c1, c2)
    
    dist = [10000000000.0] * n
    return solve(mat, n, 0, dist, k)