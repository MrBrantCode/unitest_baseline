"""
QUESTION:
A line on the plane is described by an equation Ax + By + C = 0. You are to find any point on this line, whose coordinates are integer numbers from  - 5·1018 to 5·1018 inclusive, or to find out that such points do not exist.

Input

The first line contains three integers A, B and C ( - 2·109 ≤ A, B, C ≤ 2·109) — corresponding coefficients of the line equation. It is guaranteed that A2 + B2 > 0.

Output

If the required point exists, output its coordinates, otherwise output -1.

Examples

Input

2 5 3


Output

6 -3
"""

def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

def bezout(x, y):
    if x % y == 0:
        return (0, 1)
    else:
        (t, s) = bezout(y, x % y)
        return (s, t - x // y * s)

def find_integer_point_on_line(A, B, C):
    if A == 0:
        if C % B == 0:
            return (0, -C // B)
        else:
            return -1
    if B == 0:
        if C % A == 0:
            return (-C // A, 0)
        else:
            return -1
    if C % gcd(A, B) != 0:
        return -1
    else:
        (x, y) = bezout(A, B)
        m = -C // gcd(A, B)
        return (m * x, m * y)