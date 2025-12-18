"""
QUESTION:
Create a function called `prime_numbers(N)` that prints and returns a list of all prime numbers between 2 and N (inclusive), given an integer N as argument.
"""

def prime_numbers(N):
    primes = []
    for num in range(2, N+1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
            primes.append(num)
    return primes