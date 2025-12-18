"""
QUESTION:
Write a function named `prime_count_and_product` that takes a list of up to 1000 positive integers between 1 and 100, and returns a tuple containing the count of prime numbers and their product. A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.
"""

def prime_count_and_product(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_count = 0
    prime_product = 1
    
    for num in numbers:
        if is_prime(num):
            prime_count += 1
            prime_product *= num
    
    return prime_count, prime_product