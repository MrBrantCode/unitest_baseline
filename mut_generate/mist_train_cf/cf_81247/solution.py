"""
QUESTION:
Create a function named `largest_prime` that takes an array of integers as input and returns the largest prime number present in the array. If no prime number is found, return `None`.
"""

def largest_prime(arr):
    """Function to find the largest prime in the array"""
    def is_prime(num):
        """Function to check whether a number is prime or not"""
        if num > 1:
            # Check factors up to the square root of num
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    return False
        else:
            return False
        return True

    # Iterate over the array
    max_prime = None
    for num in arr:
        if is_prime(num):
            # Update max_prime if num is larger
            if max_prime is None or num > max_prime:
                max_prime = num
    # return max_prime or None
    return max_prime