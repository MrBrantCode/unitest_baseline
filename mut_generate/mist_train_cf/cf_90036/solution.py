"""
QUESTION:
Generate a function `sum_even_primes_in_fibonacci` that calculates the sum of all even prime numbers in the Fibonacci sequence up to the 40th term. Each term must be less than 1,000,000.
"""

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def sum_even_primes_in_fibonacci():
    """
    Calculates the sum of all even prime numbers in the Fibonacci sequence up to the 40th term.
    Each term must be less than 1,000,000.
    """
    # Initialize variables a and b to 0 and 1 respectively
    a, b = 0, 1

    # Initialize a variable to store the sum of prime numbers
    sum_prime = 0

    # Generate the Fibonacci sequence up to the 40th term
    for _ in range(40):
        # Calculate the next term by adding the previous two terms
        next_term = a + b
        
        # Check if the term is even and prime
        if next_term % 2 == 0 and is_prime(next_term):
            # Add the prime term to the sum
            sum_prime += next_term
        
        # Update the values of a and b
        a, b = b, next_term

    return sum_prime