"""
QUESTION:
Given a set of coordinates points of the form [p, q] and a line L of the form ax + by + c = 0. The task is to find a point on a given line for which the sum of distances from a given set of coordinates is minimum. 
 
Example 1:
Input:
L = {1, -1, -3}
points[] = {{-3, 2}, {-1, 0}, 
            {-1, 2}, {1, 2}, {3, 4}}
Output: 20.77
Explanation: In above figure optimum location of 
point of x - y - 3 = 0 line is (2, -1), whose 
total distance with other points is 20.77, 
which is minimum obtainable total distance.
Example 2:
Input:
L = {2, 1, 4}
points[] = {{-1, 2}, {1, 3},{2, 4}}
Output: 11.20
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function findOptimumCost() which takes a line L and coordinates and returns an double up to 2 decimal places as output.
Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N)
 
Constraints:
1 <= N <= 10^{5}
-10^{3 }<= point[i] <= 10^{3}
"""

from typing import List
from math import sqrt

def find_optimum_cost(line: List[int], points: List[List[int]]) -> float:
    def distance(x1, x2, y1, y2):
        x_diff = (x1 - x2) * (x1 - x2)
        y_diff = (y1 - y2) * (y1 - y2)
        return sqrt(x_diff + y_diff)

    def compute(x, line, points):
        (a, b, c) = line
        y = -(a * x + c) / b
        res = 0.0
        for (x1, y1) in points:
            res += distance(x, x1, y, y1)
        return res

    low = -1000
    high = 1000
    eps = 0.001
    if line[1] == 0:
        return float('inf')
    while high - low > eps:
        mid1 = low + (high - low) / 3
        mid2 = high - (high - low) / 3
        dist1 = compute(mid1, line, points)
        dist2 = compute(mid2, line, points)
        if dist1 < dist2:
            high = mid2
        else:
            low = mid1
    avg = (low + high) / 2
    return round(compute(avg, line, points), 2)