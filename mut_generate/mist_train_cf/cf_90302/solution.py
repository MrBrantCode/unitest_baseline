"""
QUESTION:
Create a function called `print_prime_multiplication_table` that prints a multiplication table of a given size, but only includes the products of two prime numbers. The function should take one argument: `size`, which represents the dimensions of the table. The table should be printed with tab-separated values for better readability.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_prime_multiplication_table(size):
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if is_prime(i) and is_prime(j):
                print(i * j, end='\t')
            else:
                print('\t', end='')
        print()