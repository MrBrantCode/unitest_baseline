"""
QUESTION:
Watson gives a circle and a triangle in a 2-dimensional plane to Sherlock. Sherlock has to tell if they intersect/touch each other. 

The circle is centered at $(x_c,y_c)$ and has radius $\mbox{R}$.   

Input Format 

The first line contains $\mathbf{T}$, the number of test cases. 

Each test case consists of $x_c$, $\boldsymbol{y}_{c}$ and $\mbox{R}$ in one line. 

The next three lines each contains $x_i,y_i$ denoting the vertices of the triangle.   

Output Format 

For each test case, print YES if the triangle touches or intersects the circle; otherwise, print NO.   

Constraints 

$1\leq T\leq30000$ 

$1\leq R\leq2000$ 

$-2000\leq x_c,y_c\leq2000$ 

$-5000\leq x_i,y_i\leq5000$ 

Note: There will be no degenerate triangles (i.e. triangles with area 0)  

Sample Input  

2
0 0 10
10 0
15 0
15 5
0 0 10
0 0
5 0
5 5

Sample Output    

YES
NO

Explanation 

In the first case, the triangle is touching the circle. In the second case, it neither touches nor intersects the circle.
"""

from fractions import Fraction as F

def does_triangle_intersect_circle(circle_center, radius, triangle_vertices):
    def check(x1, y1, x2, y2, r):
        (x, y) = (x1, y1)
        dx = x2 - x
        dy = y2 - y
        A = dx ** 2 + dy ** 2
        halfB = x * dx + y * dy
        opt = F(-halfB, A)
        if opt < 0:
            opt = 0
        elif opt > 1:
            opt = 1
        least_dist = (x + dx * opt) ** 2 + (y + dy * opt) ** 2
        max_dist = max(x1 ** 2 + y1 ** 2, x2 ** 2 + y2 ** 2)
        return least_dist <= r ** 2 <= max_dist
    
    (x_c, y_c) = circle_center
    (x1, y1), (x2, y2), (x3, y3) = triangle_vertices
    
    # Shift the triangle vertices relative to the circle center
    x1 -= x_c
    y1 -= y_c
    x2 -= x_c
    y2 -= y_c
    x3 -= x_c
    y3 -= y_c
    
    # Check if any of the triangle edges intersect or touch the circle
    return check(x1, y1, x2, y2, radius) or check(x2, y2, x3, y3, radius) or check(x3, y3, x1, y1, radius)