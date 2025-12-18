"""
QUESTION:
Given a set of N integer points on the Cartesian plane. Your task is to find an integer point satisfying its sum of distances to N given points (S) is minimum.

------ Input ------ 

There are several test cases (fifteen at most), each formed as follows:
The first line contains a positive integer N (N ≤ 2,000).
N lines follow, each containing a pair of integers (each having an absolute value of 10^{9} at most) describing coordinates of a given point.

The input is ended with N = 0.

------ Output ------ 

For each test case, output on a line a real number (with exactly 6 decimal places) which is the respective minimum sum S found.

----- Sample Input 1 ------ 
3
1 1
2 2
3 3
5
1 4
2 3
5 2
3 5
4 1
0

----- Sample Output 1 ------ 
2.828427
9.640986
"""

from math import sqrt, floor, ceil

def find_minimum_sum_of_distances(points):
    N = len(points)
    if N == 0:
        return 0.0
    
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    
    xo = 0.0
    yo = 0.0
    disto = 42.0
    distn = 41.0
    
    for it in range(25):
        xn = 0.0
        yn = 0.0
        for i in range(N):
            di = sqrt((x[i] - xo) ** 2 + (y[i] - yo) ** 2)
            if di < 1e-12:
                di = 1e-12
            xn += x[i] / di
            yn += y[i] / di
        
        d = 0.0
        for i in range(N):
            di = sqrt((x[i] - xo) ** 2 + (y[i] - yo) ** 2)
            if di < 1e-12:
                di = 1e-12
            d += 1.0 / di
        
        xn /= d
        yn /= d
        xo = xn
        yo = yn
        disto = distn
        distn = 0.0
        for i in range(N):
            distn += sqrt((x[i] - xo) ** 2 + (y[i] - yo) ** 2)
    
    dist = [0.0, 0.0, 0.0, 0.0]
    for i in range(N):
        dist[0] += sqrt((x[i] - floor(xo)) ** 2 + (y[i] - floor(yo)) ** 2)
    for i in range(N):
        dist[1] += sqrt((x[i] - floor(xo)) ** 2 + (y[i] - ceil(yo)) ** 2)
    for i in range(N):
        dist[2] += sqrt((x[i] - ceil(xo)) ** 2 + (y[i] - floor(yo)) ** 2)
    for i in range(N):
        dist[3] += sqrt((x[i] - ceil(xo)) ** 2 + (y[i] - ceil(yo)) ** 2)
    
    return round(min(dist), 6)