"""
QUESTION:
Write a function `print_pyramid(num_lines)` that takes an integer `num_lines` as input and prints a pyramid structure with `num_lines` number of lines. Each line of the pyramid should consist of consecutive prime numbers arranged in descending order.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_pyramid(num_lines):
    current_line = 1
    current_num = 2
    while current_line <= num_lines:
        primes = []
        while len(primes) < current_line:
            if is_prime(current_num):
                primes.append(current_num)
            current_num += 1
        print(*primes[::-1])
        current_line += 1