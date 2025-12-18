"""
QUESTION:
Create a function called `largest_common_divisor` that takes two integers A and B as input and returns their largest common divisor. Implement the solution without using any built-in functions or libraries for calculating the greatest common divisor.
"""

def largest_common_divisor(A, B):
    # Ensure A is greater than or equal to B
    if B > A:
        A, B = B, A

    # Find the largest common divisor using Euclidean algorithm
    while B != 0:
        A, B = B, A % B

    return A