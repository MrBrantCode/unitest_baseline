"""
QUESTION:
Create a function `prime_numbers_and_sum(a, b, c)` that takes three integers as input and returns a dictionary containing their sum, a list of prime numbers among them, and the count of prime numbers. The function should handle any errors or exceptions that occur during its execution.
"""

def prime_numbers_and_sum(a, b, c):
    # Function to check whether a number is prime or not
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
            
        return True

    numbers = [a, b, c]
    sum_of_numbers = sum(numbers)
    prime_numbers = [num for num in numbers if is_prime(num)]
    prime_count = len(prime_numbers)

    return {"Sum": sum_of_numbers, "Primes": prime_numbers, "PrimeCount": prime_count}