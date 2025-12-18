"""
QUESTION:
AtCoDeer the deer found N rectangle lying on the table, each with height 1.
If we consider the surface of the desk as a two-dimensional plane, the i-th rectangle i(1≤i≤N) covers the vertical range of [i-1,i] and the horizontal range of [l_i,r_i], as shown in the following figure:

AtCoDeer will move these rectangles horizontally so that all the rectangles are connected.
For each rectangle, the cost to move it horizontally by a distance of x, is x.
Find the minimum cost to achieve connectivity.
It can be proved that this value is always an integer under the constraints of the problem.

-----Constraints-----
 - All input values are integers.
 - 1≤N≤10^5
 - 1≤l_i<r_i≤10^9

-----Partial Score-----
 - 300 points will be awarded for passing the test set satisfying 1≤N≤400 and 1≤l_i<r_i≤400.

-----Input-----
The input is given from Standard Input in the following format:
N
l_1 r_1
l_2 r_2
:
l_N r_N

-----Output-----
Print the minimum cost to achieve connectivity.

-----Sample Input-----
3
1 3
5 7
1 3

-----Sample Output-----
2

The second rectangle should be moved to the left by a distance of 2.
"""

def minimum_connectivity_cost(N, rectangles):
    INF = 10 ** 18
    from heapq import heappush, heappop
    
    (l0, r0) = rectangles[0]
    L = [-l0 + 1]
    R = [l0 - 1]
    s = t = 0
    res = 0
    
    for i in range(N - 1):
        (l0, r0) = rectangles[i]
        (l1, r1) = rectangles[i + 1]
        s += r1 - l1
        t += r0 - l0
        
        if -s - L[0] <= l1 - 1 <= t + R[0]:
            heappush(L, -l1 + 1 - s)
            heappush(R, l1 - 1 - t)
        elif l1 - 1 < -s - L[0]:
            heappush(L, -l1 + 1 - s)
            heappush(L, -l1 + 1 - s)
            p = -heappop(L) - s
            heappush(R, p - t)
            res += p - (l1 - 1)
        elif t + R[0] < l1 - 1:
            heappush(R, l1 - 1 - t)
            heappush(R, l1 - 1 - t)
            p = heappop(R) + t
            heappush(L, -p - s)
            res += l1 - 1 - p
    
    return res