"""
QUESTION:
Write a function `multiplication_square_reverse(n, m)` that prints out a multiplication square in reverse order starting from `n*m` down to `1`. The function should handle and validate the input arguments `n` and `m`, which represent the dimensions of the square. Both `n` and `m` should be positive integers, and default to 10 if not provided.
"""

def multiplication_square_reverse(n=10, m=10):
    # Check if inputs are integers
    if not isinstance(n, int) or not isinstance(m, int):
        print("Both dimensions should be integers.")
        return

    # Check if inputs are positive
    if n <= 0 or m <= 0:
        print("Both dimensions should be positive.")
        return

    # Generate the multiplication square
    for i in range(n, 0, -1):
        for j in range(m, 0, -1):
            print(i*j, end='\t')
        print()