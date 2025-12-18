"""
QUESTION:
Example

Input

1


Output

)(
"""

import bisect

def generate_parentheses_sequence(n: int) -> str:
    a = [0]
    for i in range(1, 50000):
        a.append(a[-1] + i)
    
    t = bisect.bisect_left(a, n)
    r = [1] * t + [0] * t
    
    for i in range(t):
        ai = a[t - i]
        ti = t + i
        if n < ai:
            ts = min(t, ai - n)
            (r[ti], r[ti - ts]) = (r[ti - ts], r[ti])
            n -= t - ts
        else:
            break
    
    return ''.join(map(lambda x: '()'[x], r))