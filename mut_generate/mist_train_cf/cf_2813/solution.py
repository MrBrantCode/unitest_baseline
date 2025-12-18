"""
QUESTION:
Create a function `print_message(n)` that takes an integer `n` as input, checks if it's a prime number and greater than 100, and if so, prints the message "Hello, World!" `n` times.
"""

def print_message(n):
    message = "Hello, World!"
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    if n > 100:
        for _ in range(n):
            print(message)