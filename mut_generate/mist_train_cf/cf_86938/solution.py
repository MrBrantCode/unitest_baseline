"""
QUESTION:
Implement a function called `prime_numbers` that takes an integer `n` as input and does the following: 
- Iterates through all numbers from 2 to `n` (inclusive) using a single loop, skipping any numbers divisible by 5 or 7.
- For each non-skipped number, checks if it's a prime number.
- If a prime number is found, adds it to a running sum and increments a counter.
- After the loop, prints all the prime numbers found (excluding those divisible by 5 or 7), their sum, and the total count of prime numbers.
- The function should also check if `n` itself is a prime number and output the result.
The function should be implemented without using any built-in functions or libraries for prime number calculations.
"""

def prime_numbers(n):
    """
    This function generates a list of prime numbers up to 'n', 
    excluding those divisible by 5 or 7, and calculates their sum and count.

    Args:
    n (int): The upper limit for prime number generation.

    Returns:
    None
    """

    def check_prime(num):
        """Helper function to check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                return False
        return True

    count = 0
    sum_primes = 0
    primes = []

    for num in range(2, n+1):
        if num % 5 == 0 or num % 7 == 0:
            continue
        if check_prime(num):
            primes.append(num)
            count += 1
            sum_primes += num

    print("Prime numbers up to", n, ":", primes)
    print("Sum of prime numbers:", sum_primes)
    print("Total count of prime numbers:", count)

    print(n, "is a prime number." if check_prime(n) else n, "is not a prime number.")