"""
QUESTION:
New AtCoder City has an infinite grid of streets, as follows:

* At the center of the city stands a clock tower. Let (0, 0) be the coordinates of this point.
* A straight street, which we will call East-West Main Street, runs east-west and passes the clock tower. It corresponds to the x-axis in the two-dimensional coordinate plane.
* There are also other infinitely many streets parallel to East-West Main Street, with a distance of 1 between them. They correspond to the lines \ldots, y = -2, y = -1, y = 1, y = 2, \ldots in the two-dimensional coordinate plane.
* A straight street, which we will call North-South Main Street, runs north-south and passes the clock tower. It corresponds to the y-axis in the two-dimensional coordinate plane.
* There are also other infinitely many streets parallel to North-South Main Street, with a distance of 1 between them. They correspond to the lines \ldots, x = -2, x = -1, x = 1, x = 2, \ldots in the two-dimensional coordinate plane.



There are N residential areas in New AtCoder City. The i-th area is located at the intersection with the coordinates (X_i, Y_i) and has a population of P_i. Each citizen in the city lives in one of these areas.

The city currently has only two railroads, stretching infinitely, one along East-West Main Street and the other along North-South Main Street.
M-kun, the mayor, thinks that they are not enough for the commuters, so he decides to choose K streets and build a railroad stretching infinitely along each of those streets.

Let the walking distance of each citizen be the distance from his/her residential area to the nearest railroad.
M-kun wants to build railroads so that the sum of the walking distances of all citizens, S, is minimized.

For each K = 0, 1, 2, \dots, N, what is the minimum possible value of S after building railroads?

Constraints

* 1 \leq N \leq 15
* -10 \ 000 \leq X_i \leq 10 \ 000
* -10 \ 000 \leq Y_i \leq 10 \ 000
* 1 \leq P_i \leq 1 \ 000 \ 000
* The locations of the N residential areas, (X_i, Y_i), are all distinct.
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
X_1 Y_1 P_1
X_2 Y_2 P_2
:  :  :
X_N Y_N P_N


Output

Print the answer in N+1 lines.
The i-th line (i = 1, \ldots, N+1) should contain the minimum possible value of S after building railroads for the case K = i-1.

Examples

Input

3
1 2 300
3 3 600
1 4 800


Output

2900
900
0
0


Input

5
3 5 400
5 3 700
5 5 1000
5 7 700
7 5 400


Output

13800
1600
0
0
0
0


Input

6
2 5 1000
5 2 1100
5 5 1700
-2 -5 900
-5 -2 600
-5 -5 2200


Output

26700
13900
3200
1200
0
0
0


Input

8
2 2 286017
3 1 262355
2 -2 213815
1 -3 224435
-2 -2 136860
-3 -1 239338
-2 2 217647
-1 3 141903


Output

2576709
1569381
868031
605676
366338
141903
0
0
0
"""

def calculate_minimum_walking_distances(n, residential_areas):
    xcal = [[0] * n for _ in range(1 << n)]
    ycal = [[0] * n for _ in range(1 << n)]
    
    for i in range(1 << n):
        for j in range(n):
            xcal[i][j] = abs(residential_areas[j][0])
            ycal[i][j] = abs(residential_areas[j][1])
            for k in range(n):
                if i >> k & 1:
                    xcal[i][j] = min(xcal[i][j], abs(residential_areas[j][0] - residential_areas[k][0]))
                    ycal[i][j] = min(ycal[i][j], abs(residential_areas[j][1] - residential_areas[k][1]))
            xcal[i][j] *= residential_areas[j][2]
            ycal[i][j] *= residential_areas[j][2]
    
    ans = [float('inf')] * (n + 1)
    
    for i in range(1 << n):
        count = 0
        for j in range(n):
            if i >> j & 1:
                count += 1
        j = i
        while j >= 0:
            j &= i
            cost = 0
            for k in range(n):
                if not i >> k & 1:
                    cost += min(xcal[j][k], ycal[i - j][k])
                if cost > ans[count]:
                    break
            ans[count] = min(ans[count], cost)
            j -= 1
    
    return ans