"""
QUESTION:
Create a function called `find_prime_numbers(n)` that returns a list of all prime numbers under the nth number, where n is a positive integer greater than 1. This function should utilize the `is_prime(n)` function, which takes an integer as input and returns True if it is a prime number and False otherwise. The function should handle input validation by checking if the input value of n is greater than 1. If it is not, print an error message and exit the function.
"""

def find_prime_numbers(n):
    if n < 2:
        print("Error: n should be greater than 1.")
        return
    
    is_prime = [True] * n
    is_prime[0] = False  

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i-1]:
            for j in range(i*i, n, i):
                is_prime[j-1] = False

    primes = [i+1 for i in range(n-1) if is_prime[i]]
    return primes