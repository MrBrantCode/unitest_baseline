"""
QUESTION:
Example

Input

2
10 10


Output

40.00000000
"""

def calculate_max_distance(n, a):
    if n == 1:
        return a[0] * 2
    
    r = a[0] * 2
    p = [a[0]]
    
    for i in range(1, n):
        c = a[i]
        cp = c
        for j in range(i):
            b = a[j]
            bp = p[j]
            t = abs(b - c)
            u = ((b + c) ** 2 - t ** 2) ** 0.5
            tp = bp + u
            if cp < tp:
                cp = tp
        p.append(cp)
        if r < cp + c:
            r = cp + c
    
    return r