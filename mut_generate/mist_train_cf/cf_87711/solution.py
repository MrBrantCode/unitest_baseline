"""
QUESTION:
Write a function `print_prime_numbers(start, end)` that prints all prime numbers between `start` and `end` (exclusive), where `start` is greater than `end`. If `start` is not greater than `end`, print an error message. If no prime numbers are found, print a corresponding message.
"""

def print_prime_numbers(start, end):
    if start <= end:
        print("The first integer must be greater than the second integer.")
        return
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = [n for n in range(start, end - 1, -1) if is_prime(n)]
    if prime_numbers:
        print("Prime numbers between", start, "and", end, "are:")
        for prime in prime_numbers:
            print(prime)
    else:
        print("There are no prime numbers between", start, "and", end)