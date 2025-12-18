"""
QUESTION:
Takahashi is drawing a segment on grid paper.

From a certain square, a square that is x squares to the right and y squares above, is denoted as square (x, y).

When Takahashi draws a segment connecting the lower left corner of square (A, B) and the lower left corner of square (C, D), find the number of the squares crossed by the segment.

Here, the segment is said to cross a square if the segment has non-empty intersection with the region within the square, excluding the boundary.

Constraints

* 1 \leq A, B, C, D \leq 10^9
* At least one of A \neq C and B \neq D holds.

Input

The input is given from Standard Input in the following format:


A B C D


Output

Print the number of the squares crossed by the segment.

Examples

Input

1 1 3 4


Output

4


Input

2 3 10 7


Output

8
"""

def count_crossed_squares(A: int, B: int, C: int, D: int) -> int:
    """
    Calculate the number of squares crossed by a segment connecting the lower left corners of squares (A, B) and (C, D).

    Parameters:
    A (int): The x-coordinate of the first square.
    B (int): The y-coordinate of the first square.
    C (int): The x-coordinate of the second square.
    D (int): The y-coordinate of the second square.

    Returns:
    int: The number of squares crossed by the segment.
    """
    
    def gcd(x: int, y: int) -> int:
        """Helper function to compute the greatest common divisor (GCD) of two numbers."""
        if x % y == 0:
            return y
        else:
            return gcd(y, x % y)
    
    if A == C or B == D:
        return 0
    else:
        n = gcd(abs(A - C), abs(B - D))
        e, f = abs(A - C) // n, abs(B - D) // n
        return (e + f - 1) * n