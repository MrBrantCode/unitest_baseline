"""
QUESTION:
Write a function named `largest_common_divisor` that takes two integers A and B as input and returns their greatest common divisor without using any built-in functions or libraries.
"""

def largest_common_divisor(A, B):
    # Ensure A is greater than or equal to B
    if B > A:
        A, B = B, A

    # Find the largest common divisor using Euclidean algorithm
    while B != 0:
        A, B = B, A % B

    return A