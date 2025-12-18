"""
QUESTION:
Construct a function `construct_prime_matrix` that takes a list of integers as input and returns a 2D list representing a matrix where the sum of each row and each column is equal to a prime number, if such a matrix exists. If no such matrix exists, return a message indicating the impossibility.
"""

def construct_prime_matrix(nums):
    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n**0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True

    def is_prime_matrix(matrix):
        """Check if a matrix has prime row and column sums."""
        for row in matrix:
            if not is_prime(sum(row)):
                return False
        for col in range(len(matrix[0])):
            if not is_prime(sum(matrix[row][col] for row in range(len(matrix)))):
                return False
        return True

    # Generate all permutations of the input list
    from itertools import permutations
    for perm in permutations(nums):
        # Reshape the permutation into a square matrix
        size = int(len(nums) ** 0.5)
        if size * size != len(nums):
            return "No such matrix exists."
        matrix = [perm[i * size:(i + 1) * size] for i in range(size)]
        # Check if the matrix has prime row and column sums
        if is_prime_matrix(matrix):
            return matrix
    return "No such matrix exists."