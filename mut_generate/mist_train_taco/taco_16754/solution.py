"""
QUESTION:
Example

Input

5 3
4
2
5


Output

5
2
4
1
3
"""

def reorder_elements(n, m, E):
    s = set()
    E.reverse()
    F = []
    
    for e in E:
        if e in s:
            continue
        s.add(e)
        F.append(e)
    
    for i in range(1, n + 1):
        if i in s:
            continue
        F.append(i)
    
    return F