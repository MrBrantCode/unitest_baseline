"""
QUESTION:
Write a recursive function named `recursive_function` that takes an integer `n` as input and performs the following operations: 

- The function starts with `n = 20` and stops when `n = 0`.
- It excludes prime numbers from the sequence.
- For non-prime even numbers, it prints the square of the number.
- For non-prime odd numbers, it prints the cube of the number.

The function should use recursion to decrement `n` by 1 in each recursive call.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def recursive_function(n):
    if n < 0:
        return
    elif not is_prime(n):
        if n % 2 == 0:
            print(n ** 2)
        else:
            print(n ** 3)
    recursive_function(n - 1)