"""
QUESTION:
Problem

Satake doesn't like being bent.
For example, I don't like pencils, chopsticks, and bent-shaped houses, and I don't like taking actions such as turning right or left.

By the way, Satake who lives on the XY plane is $ N $ shops $ (X_ {1}, Y_ {1}), (X_ {2}, Y_ {2}), \ ldots, (X_ {N} , Y_ {N}) I was asked to shop for $. Depart from the house at coordinates $ (0, 0) $ in the direction of $ (1, 0) $, shop at all stores, and then return home. You can go around the shops in any order. As a user, Satake can perform any of the following actions as many times as you like.

1. Go as much as you like in the direction you are facing
2. When the coordinates are the same as the shop or house, rotate clockwise or counterclockwise by the desired angle on the spot.
3. When the coordinates are the same as the store, shop while maintaining the coordinates and the direction in which they are facing.



As I said earlier, Satake doesn't like to bend. To prepare your mind, find the minimum sum of the angles that Satake will rotate in Action 2. As an example, if you rotate $ 90 ^ {\ circ} $ clockwise and then $ 90 ^ {\ circ} $ counterclockwise, the sum of the angles will be $ 180 ^ {\ circ} $.

Constraints

The input meets the following conditions:

* $ 2 \ le N \ le 8 $
* $ -1000 \ le X_ {i}, Y_ {i} \ le 1000 \ quad (1 \ le i \ le N) $
* $ (X_ {i}, Y_ {i}) \ ne (0, 0) \ quad (1 \ le i \ le N) $
* $ (X_ {i}, Y_ {i}) \ ne (X_ {j}, Y_ {j}) \ quad (i \ ne j) $
* All inputs are integers

Input

The input is given in the following format:


$ N $
$ X_ {1} $ $ Y_ {1} $
$ \ vdots $
$ X_ {N} $ $ Y_ {N} $


The input consists of $ N + 1 $ lines.
The $ 1 $ line is given $ N $, which represents the number of stores to shop.
The $ N $ line starting from the $ 2 $ line is given the coordinates $ X_ {i}, Y_ {i} $ of the store where you shop, separated by blanks.

Output

Please output the minimum value of the sum of the angles that Satake rotates in degrees. However, the correct answer is given only when the absolute error from the assumed solution is $ 10 ^ {-4} $ or less.

Examples

Input

2
0 1
0 -1


Output

450.00000000


Input

3
1 0
0 1
-2 -1


Output

386.565051
"""

import math
from itertools import permutations

def calculate_minimum_rotation_angle(n, shops):
    def dot(a, b):
        return sum(list(map(lambda x: x[0] * x[1], zip(a, b))))

    ans = float('inf')
    for l in permutations(range(n), n):
        (x, y) = [0, 0]
        m = 0
        v = [1, 0]
        for i in l:
            (s, t) = shops[i]
            nv = [s - x, t - y]
            m += math.acos(dot(v, nv) / (dot(v, v) * dot(nv, nv)) ** 0.5)
            (x, y) = (s, t)
            v = [nv[0], nv[1]]
        (s, t) = (0, 0)
        nv = [s - x, t - y]
        m += math.acos(dot(v, nv) / (dot(v, v) * dot(nv, nv)) ** 0.5)
        ans = min(ans, m)
    
    return ans * 180 / math.pi