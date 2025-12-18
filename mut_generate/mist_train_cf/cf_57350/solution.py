"""
QUESTION:
Create a function named `classify_numbers` that takes a set of positive integers as input and returns three lists: perfect squares, perfect cubes, and prime numbers. The function should be able to identify and categorize numbers into these three categories.
"""

def classify_numbers(numbers):
    squares = []
    cubes = []
    primes = []

    # Function to check if a number is a perfect square
    def is_square(n):
        return n == round(n ** 0.5) ** 2

    # Function to check if a number is a perfect cube
    def is_cube(n):
        return n == round(n ** (1./3.)) ** 3

    # Function to check if a number is a prime
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in numbers:
        if is_square(num):
            squares.append(num)
        if is_cube(num):
            cubes.append(num)
        if is_prime(num):
            primes.append(num)

    return squares, cubes, primes