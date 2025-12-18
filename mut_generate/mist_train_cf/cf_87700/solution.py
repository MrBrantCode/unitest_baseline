"""
QUESTION:
Write a function named `print_multiplication_table` that prints the multiplication table of prime numbers less than or equal to 100. 

The function should take an integer `n` as input, but the value of `n` is not used in the calculation. It only checks if `n` is a positive integer and does not exceed 10^9. If `n` is not a positive integer or is too large, the function prints an error message.

The multiplication table should be formatted in a grid-like structure with each row and column labeled with the corresponding prime numbers. The function should also calculate and display the sum and product of all prime numbers in the table, as well as the product of prime numbers in each row and column. 

The function should optimize the calculation of prime numbers using an efficient algorithm.
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