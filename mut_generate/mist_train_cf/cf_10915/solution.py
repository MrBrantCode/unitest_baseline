"""
QUESTION:
Write a function `print_prime_multiplication_table(n)` that prints the multiplication table of prime numbers up to `n`, where each row and column is labeled with the corresponding prime numbers. The table should only display numbers that are prime. Additionally, the function should calculate and display the sum of all the prime numbers in the multiplication table.
"""

def print_prime_multiplication_table(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [i for i in range(2, n+1) if is_prime(i)]

    table = [[0] * (len(primes) + 1) for _ in range(len(primes) + 1)]
    for i in range(len(primes) + 1):
        if i > 0:
            table[0][i] = primes[i-1]
            table[i][0] = primes[i-1]

    for i in range(1, len(primes) + 1):
        for j in range(1, len(primes) + 1):
            table[i][j] = primes[i-1] * primes[j-1]

    for row in table:
        for cell in row:
            if is_prime(cell):
                print(cell, end="\t")
        print()

    sum_primes = sum([cell for row in table for cell in row if is_prime(cell)])
    print("Sum of prime numbers:", sum_primes)