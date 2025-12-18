"""
QUESTION:
Example

Input

5 5 4
6
3 2
4 2
5 2
1 4
3 4
5 4


Output

6
"""

from collections import defaultdict

def calculate_max_coverage(W, H, K, coordinates):
    mp = defaultdict(lambda: defaultdict(int))
    
    for (x, y) in coordinates:
        if y % 2 == 1:
            continue
        if x % 2 == 1:
            mp[y][x // 2] |= 1
            if x < W:
                mp[y][x // 2 + 1] |= 4
        else:
            mp[y][x // 2] |= 2
    
    if K < W // 2:
        return -1
    
    K -= W // 2 + 1
    r = 0
    
    for (y, mp_xs) in mp.items():
        S = list(mp_xs.items())
        S.sort()
        a = 0
        b = 10 ** 9
        prv = -1
        
        for (x, bs) in S:
            if x - prv > 1:
                a = b = min(a, b)
            v0 = bs & 1 > 0
            v1 = bs & 2 > 0
            v2 = bs & 4 > 0
            (a, b) = (min(a + v0, b + min(v0 + v2, 2 * v1)), min(a, b + v2))
            prv = x
        
        if prv < W // 2:
            c = min(a, b)
        else:
            c = a
        
        r += c
    
    ans = max((W // 2 + 1) * (H // 2) + max(r - K, 0) - K, 0)
    return ans