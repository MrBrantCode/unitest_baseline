"""
QUESTION:
Design a function called `fibonacci` that generates prime Fibonacci numbers under a given limit and another function called `is_prime` to check if a number is prime. The `fibonacci` function should return a list of prime Fibonacci numbers under the given limit and their sum. The limit should be set at 1500.
"""

def fibonacci(limit):
    def is_prime(n):
        if n == 1: 
            return False

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    fib_numbers = [0, 1]
    while fib_numbers[-1] + fib_numbers[-2] < limit:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2]) 
    return [num for num in fib_numbers[2:] if is_prime(num)], sum([num for num in fib_numbers[2:] if is_prime(num)])

# Example usage:
limit = 1500
prime_fib_numbers, total_sum = fibonacci(limit)
print("Prime Fibonacci numbers under", limit, "are:", prime_fib_numbers)
print("Sum of prime Fibonacci numbers under", limit, "is:", total_sum)