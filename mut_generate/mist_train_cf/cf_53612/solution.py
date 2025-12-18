"""
QUESTION:
Develop an algorithm that implements the following two functions: `is_prime(n)` and `is_emirp(n)`, where `n` is a given number. The `is_prime(n)` function checks if `n` is a prime number, and the `is_emirp(n)` function checks if `n` is an emirp number, i.e., a non-palindromic prime number whose reverse is also a prime number. In addition to confirming the emirp status, your algorithm should handle large prime numbers up to 10,000 and contain error checking mechanisms to validate the input and return appropriate results or error messages.

The `is_emirp(n)` function should return an error message if the input is non-numerical, negative, or non-integer. If the number is not an emirp, the function should specify if this is because the number is not prime, is a palindrome, or its reverse is not prime.

Additionally, develop a function `get_emirp_root(n)` that calculates the emirp root of `n`, which is the smallest prime number that is a part of the emirp.
"""

def entrance(n):
    """Check if n is an emirp number"""
    # check if input is valid
    if not str(n).isnumeric() or int(n) <= 0:
        return "Error: input should be a positive integer."

    n = int(n)
    # check if input is not prime
    if not is_prime(n):
        return f"{n} is not a prime number."
    
    str_n = str(n)
    # check if the number is a palindrome
    if str_n == str_n[::-1]:
        return f"{n} is a palindrome."
        
    # check if reverse of n is prime
    rev_n = int(str_n[::-1])
    if not is_prime(rev_n):
        return f"The reverse of {n}, which is {rev_n}, is not a prime number."

    return f"{n} is an Emirp number."

def is_prime(n):
    """Check if integer n is a prime"""
    # ensure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the square root of n
    # for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def get_emirp_root(n):
    """Find the emirp root of n"""
    str_n = str(int(n))
    primes_in_n = [int(str_n[i: j]) for i in range(len(str_n)) for j in range(i + 1, len(str_n) + 1) if is_prime(int(str_n[i: j]))]
    return min(primes_in_n)