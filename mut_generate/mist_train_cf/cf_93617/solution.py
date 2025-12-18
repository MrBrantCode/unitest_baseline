"""
QUESTION:
Write a function named `print_pyramid` that takes an integer `num_lines` as input and prints a pyramid structure with consecutive prime numbers, where each line consists of consecutive prime numbers. The first line has 1 prime number, the second line has 2 prime numbers, and so on, up to `num_lines`. The numbers in the pyramid should be right-aligned and separated by a space. The function should not take any other input and should not return any value.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_pyramid(num_lines):
    primes = [2]
    line_length = 1
    current_num = 3
    while len(primes) < (num_lines * (num_lines + 1)) // 2:
        if is_prime(current_num):
            primes.append(current_num)
            line_length += 1
        current_num += 1

    pyramid = []
    total_primes = 0
    for i in range(1, num_lines + 1):
        line = " ".join(map(str, primes[total_primes:total_primes + i]))
        pyramid.append(line.rjust(num_lines * 2 - 1))
        total_primes += i

    for line in pyramid:
        print(line)