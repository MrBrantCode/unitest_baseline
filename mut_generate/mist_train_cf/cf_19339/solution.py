"""
QUESTION:
Write a function called `check_prime_and_sum` that takes a positive integer as input from the user. The function should print the input number in a sentence and indicate whether it's a prime number or not. Additionally, it should calculate and print the sum of all prime numbers up to the given input. Assume the input is a positive integer.
"""

def check_prime_and_sum(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    print(f"The number {n} is {'a prime number' if is_prime(n) else 'not a prime number'}.")
    prime_sum = sum(num for num in range(2, n + 1) if is_prime(num))
    print(f"The sum of prime numbers up to {n} is {prime_sum}.")