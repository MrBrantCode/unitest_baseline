"""
QUESTION:
Write a function named `check_prime_nums` that takes a 2D array as input and returns a tuple containing the lowest prime number and its indices in the array, or a string "No prime number in the set" if no prime numbers exist. The function should handle arrays that contain negative numbers and zeros, and the indices should be zero-based.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for current in range(3, int(n ** 0.5) + 1, 2):
        if n % current == 0:
            return False
    return True

def check_prime_nums(array_2D):
    min_prime = float('inf')
    prime_indices = []

    for i in range(len(array_2D)):
        for j in range(len(array_2D[i])):
            num = array_2D[i][j]
            if is_prime(num):
                prime_indices.append((i, j))
                if num < min_prime:
                    min_prime = num

    if prime_indices:
        return min_prime, prime_indices
    else:
        return "No prime number in the set"