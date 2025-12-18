"""
QUESTION:
Implement a function `lastRemaining(n: int) -> int` that returns the last number remaining in a list of integers from 1 to n after repeatedly applying an elimination and rotation algorithm. The algorithm alternates between removing every other number from left to right and right to left, and then rotates the remaining elements by the number of eliminated elements. The rotation direction is right for rounds starting from the left and left for rounds starting from the right. The input `n` is an integer between 1 and 10^9, inclusive.
"""

def lastRemaining(n: int) -> int:
    # Initial index
    x = 0
    # Initial number of elements
    m = n
    # Initial direction, left to right
    direction = 0
    while m > 1:
        # Left to right round
        if direction == 0 or m % 2 ==1:
            x = (x + m // 2) % m
        # Right to left round
        else:
            x = x // 2
        # Decrease the number of elements
        m = m // 2
        # Switch the direction
        direction = 1 - direction
    return x+1