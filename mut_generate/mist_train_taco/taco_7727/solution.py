"""
QUESTION:
<image>

Input

The input contains two integers a, b (1 ≤ a ≤ 10, 0 ≤ b ≤ 22·a - 1) separated by a single space.

Output

Output two integers separated by a single space.

Examples

Input

1 0


Output

0 0


Input

2 15


Output

3 0


Input

4 160


Output

12 12
"""

def calculate_hilbert_coordinates(a: int, b: int) -> tuple[int, int]:
    """
    Calculate the coordinates (x, y) in a Hilbert curve based on the given parameters.

    Parameters:
    a (int): The size parameter (1 ≤ a ≤ 10).
    b (int): The position parameter (0 ≤ b ≤ 22·a - 1).

    Returns:
    tuple[int, int]: The coordinates (x, y) in the Hilbert curve.
    """
    def rotate(x: int, y: int, sx: int, sy: int, n: int) -> tuple[int, int]:
        if sy == 0:
            if sx == 1:
                x, y = n - 1 - x, n - 1 - y
            x, y = y, x
        return x, y

    x, y = 0, 0
    for i in range(a):
        sect = 2 ** i
        sx = b >> 1 & 1
        sy = (b ^ sx) & 1
        x, y = rotate(x, y, sx, sy, sect)
        x += sect * sx
        y += sect * sy
        b //= 4
    return x, y