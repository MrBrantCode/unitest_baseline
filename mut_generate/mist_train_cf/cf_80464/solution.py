"""
QUESTION:
Write a function called `cumulative_total_of_special_primes` that calculates the cumulative total of prime numbers within the range of 100 to 200, inclusive, where these prime numbers are specifically either one or two units greater than an integer squared. The function should not take any arguments.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def cumulative_total_of_special_primes():
    """Calculates the cumulative total of prime numbers within the range of 100 to 200, 
    inclusive, where these prime numbers are specifically either one or two units greater than an integer squared."""
    cumulative_total = 0
    for base in range(10, 15):
        square = base ** 2
        if is_prime(square + 1):
            cumulative_total += square + 1
        if is_prime(square + 2):
            cumulative_total += square + 2
    return cumulative_total