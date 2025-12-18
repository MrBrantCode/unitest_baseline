"""
QUESTION:
Given are N points (x_i, y_i) in a two-dimensional plane.
Find the minimum radius of a circle such that all the points are inside or on it.

-----Constraints-----
 - 2 \leq N \leq 50
 - 0 \leq x_i \leq 1000
 - 0 \leq y_i \leq 1000
 - The given N points are all different.
 - The values in input are all integers.

-----Input-----
Input is given from Standard Input in the following format:
N
x_1 y_1
:
x_N y_N

-----Output-----
Print the minimum radius of a circle such that all the N points are inside or on it.
Your output will be considered correct if the absolute or relative error from our answer is at most 10^{-6}.

-----Sample Input-----
2
0 0
1 0

-----Sample Output-----
0.500000000000000000

Both points are contained in the circle centered at (0.5,0) with a radius of 0.5.
"""

import math

def get_circle_center_and_radius(x1, y1, x2, y2, x3, y3):
    d = 2 * ((y1 - y3) * (x1 - x2) - (y1 - y2) * (x1 - x3))
    x = ((y1 - y3) * (y1 ** 2 - y2 ** 2 + x1 ** 2 - x2 ** 2) - (y1 - y2) * (y1 ** 2 - y3 ** 2 + x1 ** 2 - x3 ** 2)) / d
    y = ((x1 - x3) * (x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2) - (x1 - x2) * (x1 ** 2 - x3 ** 2 + y1 ** 2 - y3 ** 2)) / -d
    r = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
    return (x, y, r)

def find_minimum_circle_radius(points):
    n = len(points)
    ans = float('inf')
    
    # Check for circles formed by two points
    for i in range(n - 1):
        for j in range(i + 1, n):
            x = (points[i][0] + points[j][0]) / 2
            y = (points[i][1] + points[j][1]) / 2
            r = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) / 2
            flag = 1
            for k in range(n):
                if k != i and k != j:
                    if (x - points[k][0]) ** 2 + (y - points[k][1]) ** 2 > r ** 2:
                        flag = 0
                        break
            if flag == 1:
                ans = min(r, ans)
    
    # Check for circles formed by three points
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                try:
                    (x, y, r) = get_circle_center_and_radius(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1])
                    flag = 1
                    for p in range(n):
                        if p != i and p != j and p != k:
                            if (x - points[p][0]) ** 2 + (y - points[p][1]) ** 2 > r ** 2:
                                flag = 0
                                break
                    if flag == 1:
                        ans = min(r, ans)
                except:
                    continue
    
    return ans