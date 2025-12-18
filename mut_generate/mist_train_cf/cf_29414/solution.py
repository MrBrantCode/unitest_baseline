"""
QUESTION:
Implement a `BoundaryVandermonde` class with an `__init__` method that initializes the class with a given order, and a `generate_kernel` method that computes and returns the kernel of the boundary Vandermonde matrix as a list of vectors. The kernel should be generated based on the terms of a geometric progression, excluding the first and last rows which are all ones.
"""

def boundary_vandermonde_kernel(order):
    kernel = []
    for i in range(order - 1):
        vector = [1]
        for j in range(1, order):
            vector.append(i ** j)
        kernel.append(vector)
    return kernel