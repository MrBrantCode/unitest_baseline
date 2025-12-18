"""
QUESTION:
Given three non-collinear points whose co-ordinates are P(p1, p2), Q(q1, q2) and R(r1, r2) in the X-Y plane. Find the number of integral / lattice points strictly inside the triangle formed by these points.
Note - A point in X-Y plane is said to be integral / lattice point if both its co-ordinates are integral.
Example 1:
Input:
p = (0,0)
q = (0,5)
r = (5,0)
Output: 6
Explanation:
There are 6 integral points in the 
triangle formed by p, q and r.
Example 2:
Input:
p = (62,-3)
q = (5,-45)
r = (-19,-23)
Output: 1129
Explanation:
There are 1129 integral points in the 
triangle formed by p, q and r.
Your Task:
You don't need to read input or print anything. Your task is to complete the function InternalCount() which takes the three points p, q and r as input parameters and returns the number of integral points contained within the triangle formed by p, q and r.
Expected Time Complexity: O(Log_{2}10^{9})
Expected Auxillary Space: O(1)
Constraints:
-10^{9 }≤ x-coordinate, y-coordinate ≤ 10^{9}
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def get_boundary_points(a1, a2):
    if a1[0] == a2[0]:
        return abs(a1[1] - a2[1]) - 1
    if a1[1] == a2[1]:
        return abs(a1[0] - a2[0]) - 1
    return gcd(abs(a1[0] - a2[0]), abs(a1[1] - a2[1])) - 1

def count_integral_points_in_triangle(p, q, r):
    boundary = get_boundary_points(p, q) + get_boundary_points(q, r) + get_boundary_points(p, r)
    area = abs(p[0] * (q[1] - r[1]) + q[0] * (r[1] - p[1]) + r[0] * (p[1] - q[1]))
    return (area - boundary + 2) // 2 - 1