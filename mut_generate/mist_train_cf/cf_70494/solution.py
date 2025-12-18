"""
QUESTION:
Create a function named `identify_primes` that takes an array of arbitrary integers as input and returns a list of prime numbers found in the array. The function should not use built-in functions for identifying primes and should be able to efficiently handle larger arrays. The array may be empty or contain negative numbers, which should be handled as edge cases.
"""

def identify_primes(array):
    """
    This function takes an array of arbitrary integers as input and returns a list of prime numbers found in the array.
    
    Parameters:
    array (list): A list of integers
    
    Returns:
    list: A list of prime numbers
    """
    prime_numbers = []
    for num in array: 
        # Negative numbers, 0 and 1 are not primes
        if num <= 1:
            continue
        # 2 is a prime number
        elif num == 2:
            prime_numbers.append(num)
            continue
        # Even numbers are not primes
        elif num % 2 == 0:
            continue
        # Check if num is divisible by any numbers up to its square root
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                break
        # If not, then this number is prime
        else:
            prime_numbers.append(num)
    return prime_numbers