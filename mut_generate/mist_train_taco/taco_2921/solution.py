"""
QUESTION:
[Image] 


-----Input-----

The input consists of four lines, each line containing a single digit 0 or 1.


-----Output-----

Output a single digit, 0 or 1.


-----Example-----
Input
0
1
1
0

Output
0
"""

def compute_final_output(a: int, b: int, c: int, d: int) -> int:
    def op(a, b, x):
        if x == 0:
            return a | b
        elif x == 1:
            return a ^ b
        else:
            return a & b
    
    p = (1, 0, 2)
    e = op(a, b, p[0])
    f = op(c, d, p[1])
    g = op(b, c, p[2])
    h = op(a, d, p[0])
    i = op(e, f, p[2])
    j = op(g, h, p[1])
    k = op(i, j, p[0])
    
    return k