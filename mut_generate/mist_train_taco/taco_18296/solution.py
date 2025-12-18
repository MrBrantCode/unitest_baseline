"""
QUESTION:
There is a row of N walls in Geeksland. The king of Geeksland ordered Alexa to color all the walls on the occasion of New Year. Alexa can color each wall with one of the K colors. The cost associated with coloring each wall with a particular color is represented by a 2D costs array of size N * K. For example, costs[0][0] is the cost of coloring wall 0 with color 0; costs[1][2] is the cost of coloring wall 1 with color 2, and so on... Find the minimum cost to color all the walls such that no two adjacent walls have the same color.
Note: If you are not able to paint all the walls, then you should return -1.
Example 1:
Input:
N = 4, K = 3
costs[][] = {{1, 5, 7},
             {5, 8, 4},
             {3, 2, 9},
             {1, 2, 4}}
Output:
8
Explanation:
Paint wall 0 with color 0. Cost = 1
Paint wall 1 with color 2. Cost = 4
Paint wall 2 with color 1. Cost = 2
Paint wall 3 with color 0. Cost = 1
Total Cost = 1 + 4 + 2 + 1 = 8
Example 2:
Input:
N = 5, K = 1
costs[][] = {{5},
             {4},
             {9},
             {2},
             {1}}
Output:
-1
Explanation:
It is not possible to color all the walls under the given conditions.
Your Task:
Your task is to complete the function minCost() which takes a 2D integer matrix costs as the only argument and returns an integer, representing the minimum cost to paint all the walls. If you are not able to paint all the walls, then you should return -1
Expected Time Complexity: O(N*K)
Expected Space Complexity: O(N*K)
Constraints:
	0 <= N <= 10^{3}
	0 <= K <= 10^{3}
	1 <= costs[i][j] <= 10^{5}
"""

from typing import List

def min_cost_to_paint_walls(costs: List[List[int]]) -> int:
    inf = 10 ** 18
    n = len(costs)
    k = len(costs[0]) if n > 0 else 0
    
    if k == 1 and n > 1:
        return -1
    
    nmin = [[0, -1], [0, -1]]
    
    for i in range(1, n + 1):
        min1 = nmin[:]
        nmin = []
        for j in range(1, k + 1):
            mini = min1[0]
            if mini[1] == j - 1:
                mini = min1[1]
            cost = [costs[i - 1][j - 1] + mini[0], j - 1]
            nmin.append(cost)
            nmin.sort()
            nmin = nmin[:2]
    
    return nmin[0][0]