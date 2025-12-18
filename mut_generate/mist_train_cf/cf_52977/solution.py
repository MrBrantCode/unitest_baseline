"""
QUESTION:
Write a function called `is_prime_and_square` that prints the square of each prime number from 1 to 5 and returns the running total of the squares. The function should use helper function `is_prime(n)` to check if a number `n` is prime. The function should not take any arguments.
"""

# function to check if a number is prime
def is_prime(n):
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

# main function
def is_prime_and_square():
    running_total = 0
    for i in range(1, 6):
        if is_prime(i):
            square = i ** 2
            running_total += square
            print("The square of", i, "is", square)
    print("The running total of the squares is", running_total)
    return running_total