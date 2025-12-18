"""
QUESTION:
Create two functions: `fibonacci_sum(n)` and `is_prime(number)`. 

`fibonacci_sum(n)` should calculate the sum of all even-valued terms in the Fibonacci sequence up until the nth term, where n is between 1 and 1000.

`is_prime(number)` should check if a given number is prime.
"""

def fibonacci_sum(n):
    """
    Calculate the sum of all even-valued terms in the Fibonacci sequence up until the nth term.

    Args:
    n (int): The number of terms in the Fibonacci sequence (1-1000).

    Returns:
    int: The sum of even-valued terms in the Fibonacci sequence.
    """
    fibonacci_sequence = [1, 2]  # Start with the first two terms
    sum_even = 2  # Start with the sum of the first even term

    # Generate the Fibonacci sequence up to the nth term
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

        if next_term % 2 == 0:  # Check if the new term is even
            sum_even += next_term

    return sum_even


def is_prime(number):
    """
    Check if a given number is prime.

    Args:
    number (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if number < 2:  # 0 and 1 are not prime
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True