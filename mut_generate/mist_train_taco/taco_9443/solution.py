"""
QUESTION:
You are given a non-degenerate triangle (a non-degenerate triangle is a triangle with positive area). The vertices of the triangle have coordinates $(x_1, y_1)$, $(x_2, y_2)$ and $(x_3, y_3)$.

You want to draw a straight line to cut the triangle into two non-degenerate triangles. Furthermore, the line you draw should be either horizontal or vertical.

Can you draw the line to meet all the constraints?

Here are some suitable ways to draw the line:

However, these ways to draw the line are not suitable (the first line cuts the triangle into a triangle and a quadrangle; the second line doesn't cut the triangle at all; the third line is neither horizontal nor vertical):


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 10^4$) — the number of test cases.

Each test case consists of four lines. The first of them is empty. The $i$-th of the next three lines contains two integers $x_i$ and $y_i$ ($1 \le x_i, y_i \le 10^8$) — the coordinates of the $i$-th vertex of the triangle.

Additional constraint on the input: in each test case, the triangle formed by three vertices has positive area (i. e. it is non-degenerate).


-----Output-----

For each test case, print YES if it is possible to cut the triangle according to the statement, or NO otherwise. You may print each letter in any case (YES, yes, Yes will all be recognized as positive answer, NO, no and nO will all be recognized as negative answer).


-----Examples-----

Input
4
4 7
6 8
3 5
4 5
4 7
6 8
5 8
1 8
2 5
3 6
6 6
6 3
Output
YES
YES
YES
NO


-----Note-----

None
"""

def can_cut_triangle(x1, y1, x2, y2, x3, y3):
    """
    Determines if a non-degenerate triangle with vertices (x1, y1), (x2, y2), and (x3, y3)
    can be cut into two non-degenerate triangles with a horizontal or vertical line.

    Parameters:
    x1, y1 (int): Coordinates of the first vertex.
    x2, y2 (int): Coordinates of the second vertex.
    x3, y3 (int): Coordinates of the third vertex.

    Returns:
    bool: True if it is possible to cut the triangle as described, False otherwise.
    """
    # Check if any two x-coordinates are the same (vertical line)
    if x1 == x2 or x1 == x3 or x2 == x3:
        # Check if any two y-coordinates are the same (horizontal line)
        if y1 == y2 or y1 == y3 or y2 == y3:
            return False
        return True
    return False