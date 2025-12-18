"""
QUESTION:
Write a function `print_prime_multiplication_table` that takes an integer `n` as input and prints the multiplication table of the first `n` prime numbers, calculates and displays the sum of all the numbers in the multiplication table, and checks if the sum of all the numbers in the multiplication table is a prime number, printing "YES" if it is, or "NO" if it is not. The function should not take any other input.
"""

def print_prime_multiplication_table(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1

    table = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            table[i][j] = primes[i] * primes[j]

    print("Multiplication Table:")
    for row in table:
        print(" ".join(map(str, row)))

    table_sum = sum(sum(row) for row in table)
    print("Sum of all the numbers in the multiplication table:", table_sum)

    if is_prime(table_sum):
        print("YES")
    else:
        print("NO")