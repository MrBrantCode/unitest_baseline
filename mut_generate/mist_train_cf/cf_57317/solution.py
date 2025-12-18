"""
QUESTION:
Develop a function named `check_prime(n)` that determines whether a given number `n` is prime. Using this function, create a loop that continuously prompts the user to enter a number until a prime number is entered.
"""

def check_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False