"""
QUESTION:
Write a function named `main` that takes a user-provided number as input and checks if it is prime using a recursive function or an optimized primality test algorithm. The function should also display all prime numbers between 2 and the user-provided number, and check if the user-provided number is a perfect square. Additionally, the function should calculate and display the sum and product of all prime numbers between 2 and the user-provided number, handling cases where the product exceeds the limit of the data type used for calculations. The algorithm should be efficient and scalable to handle very large numbers (up to 10^12).
"""

import math

def main(num):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_perfect_square(n):
        sqrt = int(math.sqrt(n))
        return sqrt * sqrt == n

    def sum_of_primes(n):
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        return sum(primes)

    def product_of_primes(n):
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        product = 1
        for prime in primes:
            product *= prime
            if product > 10**12:
                return None
        return product

    print(f"Is {num} prime? {is_prime(num)}")

    print("Prime numbers between 2 and", num)
    for i in range(2, num + 1):
        if is_prime(i):
            print(i)

    if is_perfect_square(num):
        print(f"{num} is a perfect square")
    else:
        print(f"{num} is not a perfect square")

    print("Sum of prime numbers between 2 and", num, ":", sum_of_primes(num))

    product = product_of_primes(num)
    if product is None:
        print("Product of prime numbers exceeds the limit of the data type used for calculations.")
    else:
        print("Product of prime numbers between 2 and", num, ":", product)