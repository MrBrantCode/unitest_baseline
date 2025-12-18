"""
QUESTION:
Write a function `print_prime_numbers(start, end)` that prints the prime numbers between `start` and `end`, where `start` is greater than `end`. If there are no prime numbers in this range, print a message indicating so. The function should check if the input condition is met and print an error message if `start` is not greater than `end`.
"""

def print_prime_numbers(start, end):
    if start <= end:
        print("The first integer must be greater than the second integer.")
        return
    prime_numbers = [n for n in range(start, end - 1, -1) if n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))]
    if prime_numbers:
        print("Prime numbers between", start, "and", end, "are:")
        for prime in prime_numbers:
            print(prime)
    else:
        print("There are no prime numbers between", start, "and", end)