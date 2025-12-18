"""
QUESTION:
Problem statement

Real variables $ x_1, x_2, ..., x_N $ satisfy the following conditions.

1. $ 0 \ leq x_i \ leq 1 $ ($ 1 \ leq i \ leq N $)
2. $ w_1x_1 + w_2x_2 + ... + w_Nx_N \ leq W $



At this time, find the maximum value that $ v_1x_1 + v_2x_2 + ... + v_Nx_N $ can take. It is known that such a maximum actually exists.

Constraint

* $ 1 \ leq N \ leq 10 ^ 5 $
* $ 1 \ leq W \ leq 10 ^ 5 $
* $ -10 ^ 4 \ leq w_i \ leq 10 ^ 4 $
* $ -10 ^ 4 \ leq v_i \ leq 10 ^ 4 $



input

Input follows the following format. All given numbers are integers.


$ N $ $ W $
$ w_1 $ $ v_1 $
$ w_2 $ $ v_2 $
$ ... $
$ w_N $ $ v_N $

output

Output the maximum possible value of $ v_1x_1 + v_2x_2 + ... + v_Nx_N $ on one line. The output must not have an error greater than $ 10 ^ {-3} $.

Examples

Input

1 1
3 1


Output

0.333333


Input

2 3
3 3
1 2


Output

4.000000


Input

2 1
-1 -3
3 10


Output

3.666667
"""

import heapq

def calculate_max_value(N, W, items):
    tmpw = 0
    tmpv = 0
    minheap = []
    
    for w, v in items:
        if w < 0:
            tmpw += w
            tmpv += v
            w *= -1
            v *= -1
        if v > 0:
            if w == 0:
                tmpv += v
            else:
                heapq.heappush(minheap, (-(v / w), w, v))
    
    while W - tmpw > 1e-09 and minheap:
        p = heapq.heappop(minheap)
        w = p[1]
        v = p[2]
        x = min(1, (W - tmpw) / w)
        tmpw += x * w
        tmpv += x * v
    
    return tmpv