"""
QUESTION:
Example

Input

2 1
WE


Output

1 2
"""

def find_optimal_split(n, m, a):
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    
    # Count 'W' and 'E' in each column
    for i in range(n):
        for j in range(m):
            if a[j][i] == 'W':
                b[i] += 1
            else:
                c[i] += 1
    
    # Prefix sum for 'E'
    for i in range(n):
        c[i + 1] += c[i]
    
    # Suffix sum for 'W'
    for i in range(n - 2, -1, -1):
        b[i] += b[i + 1]
    
    # Find the optimal split point
    m = b[0]
    r = 0
    for i in range(n):
        tm = b[i + 1] + c[i]
        if m > tm:
            r = i + 1
            m = tm
    
    return '{} {}'.format(r, r + 1)