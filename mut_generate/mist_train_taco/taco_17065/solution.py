"""
QUESTION:
You are given N non-overlapping circles in xy-plane. The radius of each circle varies, but the radius of the largest circle is not double longer than that of the smallest.

<image>

Figure 1: The Sample Input

The distance between two circles C1 and C2 is given by the usual formula

<image>

where (xi, yi ) is the coordinates of the center of the circle Ci, and ri is the radius of Ci, for i = 1, 2.

Your task is to write a program that finds the closest pair of circles and print their distance.



Input

The input consists of a series of test cases, followed by a single line only containing a single zero, which indicates the end of input.

Each test case begins with a line containing an integer N (2 ≤ N ≤ 100000), which indicates the number of circles in the test case. N lines describing the circles follow. Each of the N lines has three decimal numbers R, X, and Y. R represents the radius of the circle. X and Y represent the x- and y-coordinates of the center of the circle, respectively.

Output

For each test case, print the distance between the closest circles. You may print any number of digits after the decimal point, but the error must not exceed 0.00001.

Example

Input

4
1.0 0.0 0.0
1.5 0.0 3.0
2.0 4.0 0.0
1.0 3.0 4.0
0


Output

0.5
"""

def find_closest_circle_pair_distance(circles):
    def _get_distance(c1, c2):
        return ((c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2) ** 0.5 - c1[0] - c2[0]
    
    from itertools import combinations
    
    def _get_min_distance(circles):
        min_d = float('inf')
        for (c1, c2) in combinations(circles, 2):
            min_d = min(min_d, _get_distance(c1, c2))
        return min_d
    
    def closest_pair_distance(circles, axis=1):
        n = len(circles)
        if n <= 3:
            return _get_min_distance(circles)
        else:
            mid = n // 2
            (r, x, y) = zip(*circles)
            if len(set(x)) > len(set(y)):
                if axis == 2:
                    circles.sort(key=lambda c: c[1] - c[0])
                axis1 = 1
                axis2 = 2
            else:
                if axis == 1:
                    circles.sort(key=lambda c: c[2] - c[0])
                axis1 = 2
                axis2 = 1
            A_circles = circles[:mid]
            B_circles = circles[mid:]
            d_Amin = closest_pair_distance(A_circles.copy(), axis1)
            d_Bmin = closest_pair_distance(B_circles.copy(), axis1)
            dist = min(d_Amin, d_Bmin)
            min_d = dist
            A_circles.sort(key=lambda c: c[axis] + c[0])
            B_edge = B_circles[0][axis1] - B_circles[0][0]
            for ac in A_circles[::-1]:
                ac_r = ac[0]
                ac_edge = ac[axis1] + ac_r
                if B_edge - ac_edge >= dist:
                    break
                for bc in B_circles:
                    bc_r = bc[0]
                    if bc[axis1] - bc_r - ac_edge >= dist:
                        break
                    if abs(ac[axis2] - bc[axis2]) - ac_r - bc_r < dist:
                        min_d = min(min_d, _get_distance(ac, bc))
            return min_d
    
    return closest_pair_distance(circles)