"""
QUESTION:
Write a program which reads a rectangle and a circle, and determines whether the circle is arranged inside the rectangle. As shown in the following figures, the upper right coordinate $(W, H)$ of the rectangle and the central coordinate $(x, y)$ and radius $r$ of the circle are given.


Circle inside a rectangle


Constraints

* $ -100 \leq x, y \leq 100$
* $ 0 < W, H, r \leq 100$

Input

Five integers $W$, $H$, $x$, $y$ and $r$ separated by a single space are given in a line.

Output

Print "Yes" if the circle is placed inside the rectangle, otherwise "No" in a line.

Examples

Input

5 4 2 2 1


Output

Yes


Input

5 4 2 4 1


Output

No
"""

def is_circle_inside_rectangle(W: int, H: int, x: int, y: int, r: int) -> str:
    if r <= x <= W - r and r <= y <= H - r:
        return 'Yes'
    else:
        return 'No'