"""
QUESTION:
Example

Input

2
1 2


Output

2
"""

def find_max_consecutive_product(n, a):
    r = -1
    for i in range(n):
        b = a[i]
        for c in a[i + 1:]:
            t = b * c
            if r >= t:
                continue
            s = str(t)
            if all([int(s[k]) == int(s[k + 1]) - 1 for k in range(len(s) - 1)]):
                r = t
    return r