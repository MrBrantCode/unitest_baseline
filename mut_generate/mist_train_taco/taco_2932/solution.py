"""
QUESTION:
There is a polyline going through points (0, 0) – (x, x) – (2x, 0) – (3x, x) – (4x, 0) – ... - (2kx, 0) – (2kx + x, x) – .... 

We know that the polyline passes through the point (a, b). Find minimum positive value x such that it is true or determine that there is no such x.

Input

Only one line containing two positive integers a and b (1 ≤ a, b ≤ 109).

Output

Output the only line containing the answer. Your answer will be considered correct if its relative or absolute error doesn't exceed 10 - 9. If there is no such x then output  - 1 as the answer.

Examples

Input

3 1


Output

1.000000000000


Input

1 3


Output

-1


Input

4 1


Output

1.250000000000

Note

You can see following graphs for sample 1 and sample 3. 

<image> <image>
"""

def find_minimum_x(a: int, b: int) -> float:
    if a < b:
        return -1
    elif a == b:
        return a
    else:
        i1 = (a + b) // (2 * b)
        i2 = (a - b) // (2 * b)
        if i2 != 0:
            p = (a + b) / 2
            q = (a - b) / 2
            return min(p / i1, q / i2)
        else:
            return (a + b) / (2 * i1)