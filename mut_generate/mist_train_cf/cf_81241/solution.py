"""
QUESTION:
Write a function `product_of_primes` to calculate the product of all prime numbers in an array. The function should handle arrays of up to 10^6 elements. You must implement your own algorithm for prime number checking without using any library methods. 

Note: While the function name suggests a recursive implementation, due to the size limitation of the call stack, an iterative method is preferred to avoid potential stack overflow errors.
"""

def product_of_primes(input_array):
    """Return the product of all prime numbers in the array."""
    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    product = 1
    for num in input_array:
        if is_prime(num):
            product *= num
    return product