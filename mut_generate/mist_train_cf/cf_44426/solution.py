"""
QUESTION:
Construct a Python function called `prime_factorial` that takes a list of numbers as input and returns a new list containing the factorial values of the prime numbers in the input list. The function should ignore non-integer values in the input list and handle them without raising an error.
"""

def prime_factorial(nums):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, n):
                if (n % i) == 0:
                    return False
            return True

    result = []
    for n in nums:
        if isinstance(n, int):
            if is_prime(n):
                result.append(factorial(n))
    return result