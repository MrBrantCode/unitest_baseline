"""
QUESTION:
Implement a function `fibonacci_with_prime_sum` that takes an integer `n` as input and prints the Fibonacci series up to the nth term along with the sum of the prime numbers in the series. The function should use a helper function `is_prime` to check if a number is prime. The Fibonacci series should start with the first two terms [0, 1] and each subsequent term should be the sum of the previous two terms. The function should print the Fibonacci series and the sum of prime numbers separately.
"""

def fibonacci_with_prime_sum(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    fib_series = [0, 1]  # Initialize the Fibonacci series with the first two terms
    prime_sum = 0

    for i in range(2, n):
        fib_term = fib_series[i-1] + fib_series[i-2]
        fib_series.append(fib_term)

        if is_prime(fib_term):
            prime_sum += fib_term

    print("Fibonacci series up to the", n, "term:")
    for term in fib_series:
        print(term, end=" ")

    print("\nSum of prime numbers in the Fibonacci series:", prime_sum)