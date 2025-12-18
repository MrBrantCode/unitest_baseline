"""
QUESTION:
Create a function called `apply_to_primes` that takes an array of integers and a function as input. Apply the given function to each element in the array that is a prime number, and return a new array containing the results. The input array contains integers and the given function takes one integer argument. The output array should only contain the results of applying the function to prime numbers from the input array.
"""

def apply_to_primes(arr, func):
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    """Apply a given function to each prime number in an array and return the results."""
    return [func(num) for num in arr if is_prime(num)]