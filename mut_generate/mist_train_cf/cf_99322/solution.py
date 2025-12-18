"""
QUESTION:
Write a function named `generate_multiplication_table` that generates a multiplication table for prime numbers less than or equal to the given numbers. The function should take a list of integers `numbers` and an optional string `output_format` ("decimal" or "binary") as inputs. The function should return a 2D list representing the multiplication table, with the first row and first column labeled with the respective prime numbers. The function should also handle inputs in both decimal and hexadecimal formats.
"""

def generate_multiplication_table(numbers, output_format="decimal"):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
        return True

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