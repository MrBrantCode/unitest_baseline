"""
QUESTION:
Implement a function `fibonacci(n)` that prints the first `n` numbers in the Fibonacci series and the sum of the prime numbers within the series. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def fibonacci(n):
    def is_prime(num):
        # Handle base cases
        if num < 2:
            return False
        if num == 2:
            return True

        # Check divisibility up to square root of the number
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False

        return True

    # Initialize variables
    a, b = 0, 1
    sum_primes = 0

    # Print the first n Fibonacci numbers
    for _ in range(n):
        # Print the current Fibonacci number
        print(a)

        # Update the sum if the current Fibonacci number is prime
        if is_prime(a):
            sum_primes += a

        # Update Fibonacci numbers
        a, b = b, a + b

    # Print the sum of prime numbers
    print("Sum of prime numbers:", sum_primes)