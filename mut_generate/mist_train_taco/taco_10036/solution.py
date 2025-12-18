"""
QUESTION:
Given the value of n, print the n'th prime number.

Input : A single integer n. 
Output : A single number which is the n'th prime number.
Constraints : 
1 ≤ n ≤ 1000

SAMPLE INPUT
2

SAMPLE OUTPUT
3

Explanation

The first few prime numbers are:
2,3,5,7. So, the answer is 3.
"""

def find_nth_prime(n):
    """
    Finds the nth prime number.

    Parameters:
    n (int): The position of the prime number to find.

    Returns:
    int: The nth prime number.
    """
    if n < 1 or n > 1000:
        raise ValueError("Input n must be between 1 and 1000 inclusive.")
    
    primes = []
    num = 2
    
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    
    return primes[-1]

def is_prime(num):
    """
    Checks if a number is prime.

    Parameters:
    num (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True