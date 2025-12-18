"""
QUESTION:
Convex Hull of a set of points, in 2D plane, is a convex polygon with minimum area such that each point lies either on the boundary of polygon or inside it. Now given a set of points the task is to find the convex hull of points.
 
Example 1:
Input: points_list = {{1,2},{3,1},{5,6}}
Output: {{1,2},{3,1},{5,6}}
Example 2:
Input : points_list = {{5,1},{4,4},{1,2}}
Output: {{1,2},{4,4},{5,1}}
 
Your Task:
You don't need to read or print anything. Your task is to complete the function FindConvexHull() which takes points_list as input parameter and returns Convex Hull of given points in a list. If not possible returns a list containing -1.
 
Expected Time Complexity: O(nlog(n))
Expected Space Complexity: O(n) where n = total no. of points
 
Constraints:
1 <= n <= 10^{4}
-10^{5} <= x, y <= 10^{5}
"""

def find_convex_hull(points_list):
    def orientation(P, Q, R):
        ((xp, yp), (xq, yq), (xr, yr)) = (P, Q, R)
        return xq * (yr - yp) + xp * (yq - yr) + xr * (yp - yq)
    
    if len(points_list) < 3:
        return [[-1]]
    
    points_list.sort()
    lower = []
    upper = []
    
    for r in points_list:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], r) <= 0:
            lower.pop()
        lower.append(r)
    
    for r in reversed(points_list):
        while len(upper) >= 2 and orientation(upper[-2], upper[-1], r) <= 0:
            upper.pop()
        upper.append(r)
    
    ans = sorted(lower[:-1] + upper[:-1])
    return ans if len(ans) >= 3 else [[-1]]