"""
QUESTION:
Define a function `find_primitive_representations(n)` to calculate the cumulative count of primitive representations of perfect squares up to `n`. In this case, the primitive representation is given by the binary quadratic form `f(x,y) = x^2 + 5xy + 3y^2`, where `x` and `y` are positive integers and their greatest common divisor is 1. The function should return the total count of such primitive representations for all perfect squares up to `n`.
"""

def find_primitive_representations(n):
    grp = {}
    m1 = 26
    m2 = 60
    m = n

    def gen(s, a, b):
        if a > m or a == 0: 
            return
        if b >= 0: 
            c = a * a
            if c not in grp: 
                grp[c] = []
            grp[c].append([b, 1])
        gen(s, x * m2 + a, y * m2 + s)

    x, y = 5, 1
    a, b = 100, 1
    gen(m1, a, b)
    gen(m1, a, -b)
    gen(m1, -a, b)
    gen(m1, -a, -b)

    count = 0
    for key in grp:
        if key <= n*n:
            count += len(grp[key])

    return count