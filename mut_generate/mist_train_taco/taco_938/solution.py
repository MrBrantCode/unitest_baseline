"""
QUESTION:
Example

Input

6 3
1 0 0 1 0 1
1 3 2


Output

1
"""

import collections

def calculate_minimum_moves(n, m, b, p):
    inf = 10 ** 20
    r = inf
    
    # Generate the two possible patterns based on p
    t1 = []
    t2 = []
    for i in range(m):
        t1 += [i % 2] * p[i]
        t2 += [(i + 1) % 2] * p[i]
    
    # Check if t1 matches the count of 1s and 0s in b
    if sorted(collections.Counter(t1).items()) == sorted(collections.Counter(b).items()):
        tr = 0
        pi = 0
        for i in range(n):
            if t1[i] != 1:
                continue
            while b[pi] != 1:
                pi += 1
            tr += abs(i - pi)
            pi += 1
        r = tr
    
    # Check if t2 matches the count of 1s and 0s in b
    if sorted(collections.Counter(t2).items()) == sorted(collections.Counter(b).items()):
        tr = 0
        pi = 0
        for i in range(n):
            if t2[i] != 1:
                continue
            while b[pi] != 1:
                pi += 1
            tr += abs(i - pi)
            pi += 1
        if r > tr:
            r = tr
    
    return r