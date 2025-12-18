"""
QUESTION:
Write a function `generate_multiplication_table` that generates a multiplication table of prime numbers less than or equal to a given number. The function should take a list of integers and an optional `output_format` parameter, which can be either "decimal" or "binary". It should return a 2D table where the first row and column are labeled with the prime numbers and the rest of the table contains the products of these prime numbers. The function should also handle inputs in decimal and hexadecimal formats. Additionally, provide a function `save_table_to_csv` that saves the generated table to a CSV file.
"""

def generate_multiplication_table(numbers, output_format="decimal"):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
        return True

    from math import sqrt
    primes = [n for n in numbers if is_prime(n)]
    table = [[None] * (len(primes) + 1) for _ in range(len(primes) + 1)]
    for i in range(len(primes)):
        table[0][i+1] = primes[i]
        table[i+1][0] = primes[i]
        for j in range(i+1):
            table[i+1][j+1] = primes[i] * primes[j]
            if i != j:
                table[j+1][i+1] = table[i+1][j+1]
    if output_format == "binary":
        for i in range(len(primes)+1):
            for j in range(len(primes)+1):
                if table[i][j] is not None:
                    table[i][j] = bin(table[i][j])[2:]
    return table