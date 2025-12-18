"""
QUESTION:
Write a function `generate_table` that generates a 10x10 multiplication table where prime numbers are formatted differently from non-prime numbers. The function should also return the sum of all the prime numbers in the table. The table should be able to be printed in a visually appealing way. The numbers in the table are the products of the numbers from 1 to 10. The function should be able to check whether a number is prime or not.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_table():
    table = []
    prime_sum = 0
    for i in range(1, 11):
        row = []
        for j in range(1, 11):
            product = i * j
            if is_prime(product):
                prime_sum += product
                row.append(f"\033[1m{product}\033[0m")  # Highlight prime numbers
            else:
                row.append(str(product))
        table.append(row)
    return table, prime_sum