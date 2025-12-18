"""
QUESTION:
Write a function named `prime_numbers_2d_array` that takes a 2D array of integers as input and returns a 1D array of prime integers. The 2D array can have rows of varying lengths. The function must not use any built-in or external libraries for prime number detection.
"""

def prime_numbers_2d_array(nums):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while (i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
            i += 6
        return True

    prime_nums = []

    for row in nums:
        for val in row:
            if is_prime(val):
                prime_nums.append(val)

    return prime_nums