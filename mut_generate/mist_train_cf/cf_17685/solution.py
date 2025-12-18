"""
QUESTION:
Create a function called `print_message` that takes an integer `n` as input and prints the string "Hello, world!" `n` times, but only if `n` is a prime number.
"""

def print_message(n):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if is_prime(n):
        message = "Hello, world!"
        for _ in range(n):
            print(message)