"""
QUESTION:
Create a recursive function named `fibonacci_reverse` that calculates the Fibonacci series in reverse order and the sum of all Fibonacci numbers within the series. The function should take an integer `n` as input and return a tuple containing the Fibonacci series in reverse order and the sum of Fibonacci numbers. The function should have the following restrictions:
- The input `n` must be a prime number. If `n` is not prime, the function should return an error message.
- The function should handle cases where `n` is negative or zero.
- The time complexity of the function should be O(2^n).
- The space complexity of the function should be O(n).
- The function should use memoization to optimize recursive calls.
"""

def fibonacci_reverse(n):
    """
    Function to print the Fibonacci series in reverse order
    and calculate the sum of all Fibonacci numbers within the series
    """
    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            i = 3
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 2
            return True

    # Check if the input is a prime number
    if not is_prime(n):
        return "Input is not a prime number. Please provide a prime number."

    # Base cases
    if n <= 0:
        return []

    # Memoization dictionary to store already calculated Fibonacci numbers
    memo = {}

    def fibonacci(n):
        # Check if Fibonacci number is already calculated
        if n in memo:
            return memo[n]

        # Base cases
        if n == 1 or n == 2:
            memo[n] = 1
            return memo[n]

        # Calculate Fibonacci number
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memo[n]

    # Calculate the Fibonacci series in reverse order and sum of Fibonacci numbers
    fib_series = []
    fib_sum = 0
    for i in range(n, 0, -1):
        fib_num = fibonacci(i)
        fib_series.append(fib_num)
        fib_sum += fib_num

    return fib_series, fib_sum