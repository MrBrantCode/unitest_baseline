"""
QUESTION:
Write a function named `print_multiplication_table` that takes one integer parameter `n`. The function should print the multiplication table of prime numbers less than or equal to 100, formatted in a grid-like structure, along with the sum and product of these prime numbers, and the product of prime numbers in each row and column. The function should handle non-positive integers and very large integers (over 1 billion) by printing an error message. The input should be an integer, and non-integer inputs should also result in an error message.
"""

import math

def print_multiplication_table(n):
    if not isinstance(n, int) or n <= 0:
        print("Error: Input must be a positive integer.")
        return
    if n > 1000000000:
        print("Error: Input is too large.")
        return
    
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        for i in range(5, int(math.sqrt(num)) + 1, 6):
            if num % i == 0 or num % (i + 2) == 0:
                return False
        return True

    primes = [i for i in range(2, 101) if is_prime(i)]
    
    table = [[0] * len(primes) for _ in range(len(primes))]
    
    for i in range(len(primes)):
        for j in range(len(primes)):
            table[i][j] = primes[i] * primes[j]
    
    sum_of_primes = sum(primes)
    product_of_primes = math.prod(primes)
    
    print("Multiplication Table:")
    for i in range(len(primes)):
        print("\t" + str(primes[i]), end="")
    print("\n")
    for i in range(len(primes)):
        print(str(primes[i]), end="")
        for j in range(len(primes)):
            print("\t" + str(table[i][j]), end="")
        print("\n")
    
    print("Sum of prime numbers:", sum_of_primes)
    print("Product of prime numbers:", product_of_primes)
    print("Product of prime numbers in each row and column:")
    for i in range(len(primes)):
        row_product = math.prod(table[i])
        column_product = math.prod([table[j][i] for j in range(len(primes))])
        print("\t" + str(primes[i]) + " - Row: " + str(row_product) + ", Column: " + str(column_product))