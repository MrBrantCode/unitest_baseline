"""
QUESTION:
Write a function named `largest_square_sub_matrix` that takes an n x n matrix where each element is either 0 or 1 as input. The function should return the area of the largest square sub-matrix composed of only '1s' and with a perimeter that is a prime number. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def largest_square_sub_matrix(matrix):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    maxSide = 0
    maxArea = 0
    for row in matrix:
        consecutiveOnes = 0
        for val in row:
            if val == 1:
                consecutiveOnes += 1
            else:
                consecutiveOnes = 0
            for p in range(consecutiveOnes, maxSide, -1):
                if is_prime(4 * p) and p > maxSide:
                    maxSide = p
                    maxArea = p * p
    return maxArea