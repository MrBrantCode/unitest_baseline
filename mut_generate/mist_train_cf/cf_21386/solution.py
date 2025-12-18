"""
QUESTION:
Create a function `largest_common_divisor` that takes two positive integers A and B as input and returns their largest common divisor. The function should not use any built-in functions or libraries for calculating the greatest common divisor, the Euclidean algorithm, or any well-known algorithms for calculating the greatest common divisor. The time complexity of the function should be O(sqrt(min(A, B))).
"""

def largest_common_divisor(A, B):
    smallest = min(A, B)
    largest_divisor = 1

    for i in range(1, int(smallest**0.5) + 1):
        if A % i == 0 and B % i == 0:
            largest_divisor = i

    for i in range(int(smallest**0.5), 0, -1):
        if A % i == 0 and B % i == 0:
            largest_divisor = i
            break

    return largest_divisor