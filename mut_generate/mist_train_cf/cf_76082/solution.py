"""
QUESTION:
Create a function that generates and displays the first 10 prime numbers along with their corresponding factorials. The function should include two helper functions: `is_prime(n)` to check if a number is prime, and `factorial(n)` to calculate the factorial of a number.
"""

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    
    r = int(n ** 0.5)
    f = 5
    
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
        
    return True

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def generate_prime_factorials():
    primes = []
    i = 2
    while len(primes) < 10: 
        if is_prime(i):
            primes.append(i)
        i += 1

    for prime in primes:
        print(f'{prime}! = {factorial(prime)}')

# Function call is not included as per your requirements