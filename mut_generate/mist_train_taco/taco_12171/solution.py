"""
QUESTION:
Given two arrays X[] and Y[] of points where (X_{i}, Y_{i}) represents a point on the X-Y plane. Your task is to complete the function maxPoints which returns an integer denoting the maximum number of points that lie on the same straight line.
Example 1:
Input:
X[] = {1, 2, 3}
Y[] = {1, 2, 3}
Output: 3
Explanation:
The points are (1,1), (2,2) and (3,3).
Example 2:
Input:
X[] = {1, 3, 5, 4, 2, 1}
Y[] = {1, 2, 3, 1, 3, 4}
Output: 4
Explanation:
The points are- 
(1,1),(3,2),(5,3),(4,1),(2,3),(1,4)
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxPoints() which takes two lists of coordinates as input and returns the maximum number of points that lies on the same line.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N)
Constraints:
1 <= N <= 300
-10^{4} <= x_{i}, y_{i} <= 10^{4}^{ }
"""

def max_points_on_same_line(X, Y):
    points = [(X[i], Y[i]) for i in range(len(X))]
    n = len(points)
    
    if n < 3:
        return n
    
    max_val = 0
    
    for i in points:
        d = {}
        dups = 0
        cur_max = 0
        
        for j in points:
            if i != j:
                if j[0] == i[0]:
                    slope = 'inf'
                else:
                    slope = float(j[1] - i[1]) / float(j[0] - i[0])
                d[slope] = d.get(slope, 0) + 1
                cur_max = max(cur_max, d[slope])
            else:
                dups += 1
        
        max_val = max(max_val, cur_max + dups)
    
    return max_val