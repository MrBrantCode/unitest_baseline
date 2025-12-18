"""
QUESTION:
Create a function `circleAndTriangleOverlapping` that checks if a circle and a triangle are overlapped. The function takes 9 parameters: the radius of the circle, the x and y coordinates of the circle's center, and the x and y coordinates of the triangle's three vertices. The function should return True if the circle and the triangle are overlapped, and False otherwise. 

The circle is represented as (radius, x_center, y_center) and the triangle is represented as (x1, y1, x2, y2, x3, y3). The constraints are 1 <= radius <= 2000 and -10^4 <= x_center, y_center, x1, y1, x2, y2, x3, y3 <= 10^4.
"""

def circleAndTriangleOverlapping(radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> bool:

    # Function to calculate distance between 2 points
    def distance(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    # Function to check if a point is inside a triangle, using process "barycentric coordinates"
    def triangleContain(x1, y1, x2, y2, x3, y3, x, y):
        area = 0.5 * (-y2*x3 + y1*(-x2 + x3) + x1*(y2 - y3) + x2*y3)
        s = 1/(2*area)*(y1*x3 + x1*(-y2 + y3) - y1*x2 + y3*x2)
        t = 1/(2*area)*(x1*(y2 - y3) + y1*(x3 - x2) + y*(x2 - x3))
        return s > 0 and t > 0 and (1 - s - t) > 0
    
    gx = (x1 + x2 + x3) / 3
    gy = (y1 + y2 + y3) / 3
    d = [distance(x_center, y_center, gx, gy)]
    if triangleContain(x1, y1, x2, y2, x3, y3, x_center, y_center): return True
    if min(distance(x_center, y_center, x1, y1), distance(x_center, y_center, x2, y2), distance(x_center, y_center, x3, y3)) <= radius: return True
    if min(distance((x1+gx)/2, (y1+gy)/2, x_center, y_center), distance((x2+gx)/2, (y2+gy)/2, x_center, y_center), distance((x3+gx)/2, (y3+gy)/2, x_center, y_center)) <= radius/2: return True
    return False