"""
QUESTION:
Create a function `S(n)` that calculates the sum of the area of the uncut triangles represented by all valid quadruples with `a+b+c+d <= n`. A valid quadruple is a set of four numbers `(a, b, c, d)` that represent the areas of the four sections of a dissected triangle, where `a` is the area of the triangle between the two cut vertices, `d` is the area of the quadrilateral, `b` and `c` are the areas of the two other triangles, and `b <= c`. The quadruples can also be represented as `(u, v, w, x)` with `u^2+v^2+w^2+x^2=2*n` and `v<=w<x<u<n`. The function should return the sum of `a` for all valid quadruples. The input `n` is a positive integer and the function should return an integer. The function should be able to handle inputs up to `n=10000`.
"""

def entance(n):
    res = 0
    squares = [i*i for i in range(1, int((2*n)**0.5)+1)]
    square_set = set(squares)
    for a in squares:
        if a > n:
            break
        for b in squares:
            if a + b / 2 > n:
                break
            for c in squares[b:]:
                if a + b + c + c > 2 * n:
                    break
                d = 2 * n - a - b - c
                if d in square_set and d >= a and c <= d:
                    res += a + b
    return res