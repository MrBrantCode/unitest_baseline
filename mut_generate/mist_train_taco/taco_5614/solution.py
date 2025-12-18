"""
QUESTION:
There are N cities on a 2D plane. The coordinate of the i-th city is (x_i, y_i). Here (x_1, x_2, \dots, x_N) and (y_1, y_2, \dots, y_N) are both permuations of (1, 2, \dots, N).

For each k = 1,2,\dots,N, find the answer to the following question:

Rng is in City k. Rng can perform the following move arbitrarily many times:

* move to another city that has a smaller x-coordinate and a smaller y-coordinate, or a larger x-coordinate and a larger y-coordinate, than the city he is currently in.



How many cities (including City k) are reachable from City k?

Constraints

* 1 \leq N \leq 200,000
* (x_1, x_2, \dots, x_N) is a permutation of (1, 2, \dots, N).
* (y_1, y_2, \dots, y_N) is a permutation of (1, 2, \dots, N).
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
x_1 y_1
x_2 y_2
:
x_N y_N


Output

Print N lines. In i-th line print the answer to the question when k = i.

Examples

Input

4
1 4
2 3
3 1
4 2


Output

1
1
2
2


Input

7
6 4
4 3
3 5
7 1
2 7
5 2
1 6


Output

3
3
1
1
2
3
2
"""

def reachable_cities_count(n, coordinates):
    idx = [None] * n
    ys = [None] * n
    ans = [None] * n
    accumx = [None] * n
    accumn = [None] * n
    
    for i in range(n):
        x, y = coordinates[i]
        idx[x - 1] = i
        ys[x - 1] = y - 1
    
    accumx[-1] = ys[-1]
    for i in range(n - 2, -1, -1):
        accumx[i] = max(accumx[i + 1], ys[i])
    
    accumn[0] = ys[0]
    for i in range(1, n):
        accumn[i] = min(accumn[i - 1], ys[i])
    
    def bisect(x):
        ok = 0
        ng = n
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if accumx[mid] > x:
                ok = mid
            else:
                ng = mid
        return ok
    
    nowx = 0
    while nowx < n:
        nxtx = nowx
        tmp = bisect(ys[nowx])
        while tmp > nxtx:
            nxtx = tmp
            tmp = bisect(accumn[nxtx])
        if nxtx < nowx:
            nxtx = nowx
        for i in range(nowx, nxtx + 1):
            ans[idx[i]] = nxtx - nowx + 1
        nowx = nxtx + 1
    
    return ans