"""
QUESTION:
Peter got a new snow blower as a New Year present. Of course, Peter decided to try it immediately. After reading the instructions he realized that it does not work like regular snow blowing machines. In order to make it work, you need to tie it to some point that it does not cover, and then switch it on. As a result it will go along a circle around this point and will remove all the snow from its path.

Formally, we assume that Peter's machine is a polygon on a plane. Then, after the machine is switched on, it will make a circle around the point to which Peter tied it (this point lies strictly outside the polygon). That is, each of the points lying within or on the border of the polygon will move along the circular trajectory, with the center of the circle at the point to which Peter tied his machine.

Peter decided to tie his car to point P and now he is wondering what is the area of ​​the region that will be cleared from snow. Help him.

Input

The first line of the input contains three integers — the number of vertices of the polygon n (<image>), and coordinates of point P.

Each of the next n lines contains two integers — coordinates of the vertices of the polygon in the clockwise or counterclockwise order. It is guaranteed that no three consecutive vertices lie on a common straight line.

All the numbers in the input are integers that do not exceed 1 000 000 in their absolute value.

Output

Print a single real value number — the area of the region that will be cleared. Your answer will be considered correct if its absolute or relative error does not exceed 10 - 6. 

Namely: let's assume that your answer is a, and the answer of the jury is b. The checker program will consider your answer correct, if <image>.

Examples

Input

3 0 0
0 1
-1 2
1 2


Output

12.566370614359172464


Input

4 1 -1
0 0
1 2
2 0
1 1


Output

21.991148575128551812

Note

In the first sample snow will be removed from that area:

<image>
"""

import math
import sys

def calculate_cleared_area(n, x, y, vertices):
    def distance_two_points(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def distance_point_to_line(p1, p2, p0):
        a = p2[1] - p1[1]
        b = p1[0] - p2[0]
        c = p2[0] * p1[1] - p2[1] * p1[0]
        dist = math.fabs(a * p0[0] + b * p0[1] + c) / math.sqrt(a ** 2 + b ** 2)
        x_int = (b * (b * p0[0] - a * p0[1]) - a * c) / (a ** 2 + b ** 2)
        y_int = (a * (-b * p0[0] + a * p0[1]) - b * c) / (a ** 2 + b ** 2)
        return (dist, (x_int, y_int))

    def is_in_range(i_point, p1, p2):
        x_min = p1[0] if p1[0] <= p2[0] else p2[0]
        x_max = p1[0] if p1[0] > p2[0] else p2[0]
        y_min = p1[1] if p1[1] <= p2[1] else p2[1]
        y_max = p1[1] if p1[1] > p2[1] else p2[1]
        return x_min <= i_point[0] <= x_max and y_min <= i_point[1] <= y_max

    r_max = -sys.maxsize
    r_min = sys.maxsize
    last_d = -1
    for v in vertices:
        d = distance_two_points(v, (x, y))
        if d > r_max:
            r_max = d
        if d < r_min:
            r_min = d
    last_v = vertices[0]
    for i in range(1, n):
        (d_min, i_point) = distance_point_to_line(last_v, vertices[i], (x, y))
        if d_min < r_min and is_in_range(i_point, last_v, vertices[i]):
            r_min = d_min
        last_v = vertices[i]
    (d_min, i_point) = distance_point_to_line(last_v, vertices[0], (x, y))
    if d_min < r_min and is_in_range(i_point, last_v, vertices[0]):
        r_min = d_min
    return math.pi * (r_max ** 2 - r_min ** 2)