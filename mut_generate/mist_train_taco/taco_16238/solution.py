"""
QUESTION:
Given are a positive integer N and a sequence of length 2^N consisting of 0s and 1s: A_0,A_1,\ldots,A_{2^N-1}. Determine whether there exists a closed curve C that satisfies the condition below for all 2^N sets S \subseteq \\{0,1,\ldots,N-1 \\}. If the answer is yes, construct one such closed curve.

* Let x = \sum_{i \in S} 2^i and B_S be the set of points \\{ (i+0.5,0.5) | i \in S \\}.
* If there is a way to continuously move the closed curve C without touching B_S so that every point on the closed curve has a negative y-coordinate, A_x = 1.
* If there is no such way, A_x = 0.



For instruction on printing a closed curve, see Output below.

Constraints

* 1 \leq N \leq 8
* A_i = 0,1 \quad (0 \leq i \leq 2^N-1)
* A_0 = 1

Input

Input is given from Standard Input in the following format:


N
A_0A_1 \cdots A_{2^N-1}


Output

If there is no closed curve that satisfies the condition, print `Impossible`.

If such a closed curve exists, print `Possible` in the first line. Then, print one such curve in the following format:


L
x_0 y_0
x_1 y_1
:
x_L y_L


This represents the closed polyline that passes (x_0,y_0),(x_1,y_1),\ldots,(x_L,y_L) in this order.

Here, all of the following must be satisfied:

* 0 \leq x_i \leq N, 0 \leq y_i \leq 1, and x_i, y_i are integers. (0 \leq i \leq L)
* |x_i-x_{i+1}| + |y_i-y_{i+1}| = 1. (0 \leq i \leq L-1)
* (x_0,y_0) = (x_L,y_L).



Additionally, the length of the closed curve L must satisfy 0 \leq L \leq 250000.

It can be proved that, if there is a closed curve that satisfies the condition in Problem Statement, there is also a closed curve that can be expressed in this format.

Examples

Input

1
10


Output

Possible
4
0 0
0 1
1 1
1 0
0 0


Input

2
1000


Output

Possible
6
1 0
2 0
2 1
1 1
0 1
0 0
1 0


Input

2
1001


Output

Impossible


Input

1
11


Output

Possible
0
1 1
"""

def find_closed_curve(N, A):
    minimal_sets = []
    for n in range(1 << N):
        s = n
        is_min = A[n] == 0
        while s:
            s = s - 1 & n
            if A[n] == 1 and A[s] == 0:
                return "Impossible", None
            if A[s] == 0:
                is_min = False
        if is_min:
            minimal_sets.append(n)

    def make(nums, x):
        if not nums:
            return [(x, 0)]
        path = []
        if len(nums) == 1:
            n = nums[0]
            for i in range(x, n + 1):
                path.append((i, 0))
            path += [(n + 1, 0), (n + 1, 1), (n, 1), (n, 0)]
            for i in range(n - 1, x - 1, -1):
                path.append((i, 0))
            return path
        n = nums[0]
        for i in range(x, n + 1):
            path.append((i, 0))
        P = make(nums[1:], n + 1)
        path += P
        path += [(n, 0), (n, 1), (n + 1, 1), (n + 1, 0)]
        path += P[::-1][1:]
        path += [(n + 1, 1), (n, 1), (n, 0)]
        for i in range(n - 1, x - 1, -1):
            path += [(i, 0)]
        return path

    path = [(0, 0)]
    for n in minimal_sets:
        path += make([i for i in range(N) if n & 1 << i], 0)[1:]
    
    return "Possible", path