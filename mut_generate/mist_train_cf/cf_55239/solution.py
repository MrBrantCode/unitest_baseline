"""
QUESTION:
Create a function to print the first 10 prime numbers using a while loop. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def first_n_primes(n):
    def check_prime(num):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        return is_prime

    count = 0
    num = 2
    while count < n:
        if check_prime(num):
            print(num)
            count += 1
        num += 1