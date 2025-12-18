"""
QUESTION:
Create a function `filter_primes` that takes a list of integers `numbers` as input and returns a list of prime numbers in descending order. The input list may contain negative numbers and decimals. The function should not use any built-in functions or libraries to determine whether a number is prime. Non-integer and non-prime numbers should be excluded from the output.
"""

def filter_primes(numbers):
    prime_numbers = []
    for num in numbers:
        if isinstance(num, (int, float)):
            n = int(abs(num))
            if n < 2:
                continue
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    break
            else:
                prime_numbers.append(n)
    return sorted(prime_numbers, reverse=True)