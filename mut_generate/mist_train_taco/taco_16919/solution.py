"""
QUESTION:
Iahub has drawn a set of n points in the cartesian plane which he calls "special points". A quadrilateral is a simple polygon without self-intersections with four sides (also called edges) and four vertices (also called corners). Please note that a quadrilateral doesn't have to be convex. A special quadrilateral is one which has all four vertices in the set of special points. Given the set of special points, please calculate the maximal area of a special quadrilateral. 


-----Input-----

The first line contains integer n (4 ≤ n ≤ 300). Each of the next n lines contains two integers: x_{i}, y_{i} ( - 1000 ≤ x_{i}, y_{i} ≤ 1000) — the cartesian coordinates of ith special point. It is guaranteed that no three points are on the same line. It is guaranteed that no two points coincide. 


-----Output-----

Output a single real number — the maximal area of a special quadrilateral. The answer will be considered correct if its absolute or relative error does't exceed 10^{ - 9}.


-----Examples-----
Input
5
0 0
0 4
4 0
4 4
2 3

Output
16.000000


-----Note-----

In the test example we can choose first 4 points to be the vertices of the quadrilateral. They form a square by side 4, so the area is 4·4 = 16.
"""

def maximal_special_quadrilateral_area(points):
    """
    Calculate the maximal area of a special quadrilateral formed by a given set of special points.

    Parameters:
    points (list of tuples): A list of tuples where each tuple contains two integers (x, y) representing the coordinates of a special point.

    Returns:
    float: The maximal area of a special quadrilateral. The answer will be considered correct if its absolute or relative error does not exceed 10^-9.
    """
    
    def cross(x1, y1, x2, y2):
        return x1 * y2 - x2 * y1
    
    n = len(points)
    max_area = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            (max_left, max_right) = (0, 0)
            for k in range(n):
                if i != k and j != k:
                    (xi, yi) = points[i]
                    (xj, yj) = points[j]
                    (xk, yk) = points[k]
                    area = cross(xj - xi, yj - yi, xk - xi, yk - yi)
                    if area > 0:
                        max_left = max(max_left, area)
                    elif area < 0:
                        max_right = max(max_right, -area)
            if max_left != 0 and max_right != 0:
                max_area = max(max_area, max_left + max_right)
    
    return max_area / 2.0