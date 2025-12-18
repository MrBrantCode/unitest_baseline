"""
QUESTION:
Create a function named `print_prime_multiplication_table` that takes an integer `n` as input, generates a multiplication table of prime numbers up to `n`, and displays it in a grid-like structure. The function should only include prime numbers in the table, label each row and column with the corresponding prime numbers, and calculate the sum of all prime numbers in the table. The function should then print the multiplication table and the sum of the prime numbers.
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
        print("\t".join(str(cell) for cell in row))
    
    sum_primes = sum([cell for row in table for cell in row if is_prime(cell)])
    print("Sum of prime numbers:", sum_primes)