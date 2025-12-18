"""
QUESTION:
Write a function `print_pyramid(num_lines)` that prints a pyramid structure with consecutive prime numbers. The function should take one argument `num_lines`, which is the number of lines in the pyramid. The pyramid should be centered and each line should contain one more prime number than the previous line. The function should not take any other input and should print the pyramid directly to the console.
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
    while len(primes) < num_lines * (num_lines + 1) // 2:
        if is_prime(current_num):
            primes.append(current_num)
            line_length += 1
        current_num += 1

    index = 0
    for i in range(1, num_lines + 1):
        line = " ".join(map(str, primes[index:index+i]))
        print(line.center(num_lines * 2 - 1))
        index += i