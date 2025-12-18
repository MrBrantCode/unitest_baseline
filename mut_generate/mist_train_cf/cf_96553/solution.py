"""
QUESTION:
Create a function named `largest_common_divisor` that takes two positive integers A and B, and returns the largest common divisor between A and B without using any built-in functions or libraries for calculating the greatest common divisor, or the Euclidean algorithm. The solution should have a time complexity of O(sqrt(min(A, B))).
"""

def largest_common_divisor(A, B):
    smallest = min(A, B)
    largest_divisor = 1

    for i in range(1, smallest + 1):
        if A % i == 0 and B % i == 0:
            largest_divisor = i

    return largest_divisor