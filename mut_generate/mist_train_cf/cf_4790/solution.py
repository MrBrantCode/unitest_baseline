"""
QUESTION:
Write a function `fibonacci_reverse` that takes an integer `n` as input and returns the Fibonacci series in reverse order along with the sum of all Fibonacci numbers within the series. The function should only accept prime numbers as input and return an error message if the input is not prime. The function should have a time complexity of O(2^n) and space complexity of O(n), and use memoization to optimize recursive calls. The function should handle large input values efficiently and provide clear error messages for invalid inputs.
"""

def fibonacci_reverse(n):
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

    if not is_prime(n):
        return "Input is not a prime number. Please provide a prime number."

    memo = {}

    def fibonacci(n):
        if n in memo:
            return memo[n]
        if n == 1 or n == 2:
            memo[n] = 1
            return memo[n]
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memo[n]

    fib_series = []
    fib_sum = 0
    for i in range(n, 0, -1):
        fib_num = fibonacci(i)
        fib_series.append(fib_num)
        fib_sum += fib_num

    return fib_series, fib_sum