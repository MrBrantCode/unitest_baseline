"""
QUESTION:
Write a function `is_prime(n)` that checks if a given integer `n` is a prime number, and a function `main()` that prompts the user for an integer, reverses the integer, and then uses the `is_prime(n)` function to check if the reversed integer is prime. The `main()` function should print the reversed integer and a message indicating whether it's prime or not. The program should handle all integers as input.
"""

def entrance(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True