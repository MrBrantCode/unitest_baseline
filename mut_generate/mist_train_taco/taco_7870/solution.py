"""
QUESTION:
Consider a rectangle ABCD. Given the co-ordinates of the mid points of side AD and BC (p and q respectively) along with their length L (AD = BC = L). Find the co-ordinates of the 4 points A, B, C and D.
Example 1:
Input: L = 2, points = {{1,0},{1,2}}
Output: {{0,0},{0,2},{2,0},{2,2}}
Explanation: 
Example 2:
Input: L = 2.8284, points: {{1,1}, {-1,-1}}
Output: {{-2,0},{0,-2},{0,2},{2,0}}
Explanation: 
Your Task:
You don't need to read or print anything. Your task is to compelete the function findCornerPoints() which takes a vector of two points (p and q), and length l as input parameters and returns a vector containing the floor value of the corner points of the rectangle in sorted order.
 
Expected Time Complexity: O(1)
Expected Space Complexity: O(1)
 
Constraints:
1 <= L <= 10^{5}
1 <= p, q <= L
"""

import math

def find_corner_points(L, points):
    # Calculate the differences in coordinates
    y = points[1][0] - points[0][0]
    x = -(points[1][1] - points[0][1])
    
    # Calculate the scaling factor
    k = math.sqrt(x ** 2 + y ** 2)
    x = L / 2.0 * x / k
    y = L / 2.0 * y / k
    
    # Calculate the corner points
    result = []
    result.append([math.floor(points[0][0] - x), math.floor(points[0][1] - y)])
    result.append([math.floor(points[1][0] - x), math.floor(points[1][1] - y)])
    result.append([math.floor(points[0][0] + x), math.floor(points[0][1] + y)])
    result.append([math.floor(points[1][0] + x), math.floor(points[1][1] + y)])
    
    # Sort the result to ensure consistent output order
    result = sorted(result)
    
    return result