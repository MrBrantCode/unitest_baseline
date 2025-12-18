"""
QUESTION:
Write a program which prints the central coordinate $(p_x, p_y)$ and the radius $r$ of a circumscribed circle of a triangle which is constructed by three points $(x_1, y_1)$, $(x_2, y_2)$ and $(x_3, y_3)$ on the plane surface.

Constraints

* $-100 \leq x_1, y_1, x_2, y_2, x_3, y_3 \leq 100$
* $ n \leq 20$

Input

Input consists of several datasets. In the first line, the number of datasets $n$ is given. Each dataset consists of:

$x_1$ $y_1$ $x_2$ $y_2$ $x_3$ $y_3$

in a line. All the input are real numbers.

Output

For each dataset, print $p_x$, $p_y$ and $r$ separated by a space in a line. Print the solution to three places of decimals. Round off the solution to three decimal places.

Example

Input

1
0.0 0.0 2.0 0.0 2.0 2.0


Output

1.000 1.000 1.414
"""

def calculate_circumscribed_circle(x1, y1, x2, y2, x3, y3):
    """
    Calculate the central coordinate (px, py) and the radius r of the circumscribed circle
    of a triangle constructed by three points (x1, y1), (x2, y2), and (x3, y3) on the plane surface.

    Parameters:
    x1, y1 (float): Coordinates of the first point.
    x2, y2 (float): Coordinates of the second point.
    x3, y3 (float): Coordinates of the third point.

    Returns:
    tuple: A tuple containing (px, py, r) where px and py are the coordinates of the center
           of the circumscribed circle, and r is the radius of the circumscribed circle.
    """
    
    def cross(v1, v2):
        return v1.real * v2.imag - v1.imag * v2.real

    def get_intersection(p1, p2, p3, p4):
        a1 = p4 - p2
        b1 = p2 - p3
        b2 = p1 - p2
        s1 = cross(a1, b2) / 2
        s2 = cross(a1, b1) / 2
        return p1 + (p3 - p1) * s1 / (s1 + s2)

    # Convert points to complex numbers
    p1 = complex(x1, y1)
    p2 = complex(x2, y2)
    p3 = complex(x3, y3)

    # Midpoints
    p12 = (p1 + p2) / 2
    p13 = (p1 + p3) / 2

    # Calculate the center of the circumscribed circle
    pxy = get_intersection(p12, p13, p12 + (p2 - p1) * 1j, p13 + (p1 - p3) * 1j)

    # Calculate the radius
    r = abs(pxy - p1)

    # Return the results rounded to three decimal places
    return round(pxy.real, 3), round(pxy.imag, 3), round(r, 3)