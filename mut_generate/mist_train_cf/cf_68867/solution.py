"""
QUESTION:
Construct a method named `longest_prime_subarray` that identifies the longest continuous subarray within the supplied array, which contains only prime numbers. This function should produce the starting and ending indices of this specific subarray. The input array is expected to contain integers and the output should be a tuple of two integers representing the starting and ending indices.
"""

def is_prime(n):
    """Helper function to check if a number is prime."""
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

def longest_prime_subarray(arr):
    """Find the longest continuous subarray of prime numbers."""
    start = 0
    end = 0
    max_length = 0
    max_start = 0
    max_end = 0

    for i in range(len(arr)):
        if is_prime(arr[i]):
            end = i
            if end - start + 1 > max_length:
                max_length = end - start + 1
                max_start = start
                max_end = end
        else:
            start = i + 1

    return max_start, max_end