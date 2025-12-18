"""
QUESTION:
Create a function named `print_multiplication_table_with_prime_factors(n: int)` that takes a positive integer `n` as input. The function should print a multiplication table of size `n x n` and the prime factors of numbers 1 to `n`. The prime factors should be displayed in the format `(p1, p2, ..., pk)`, where `p1, p2, ..., pk` are the prime factors of the corresponding number. The function should not take any other inputs or return any values, only print the required output.
"""

def print_multiplication_table_with_prime_factors(n: int):
    def prime_factors(num: int):
        factors = []
        while num % 2 == 0:
            factors.append(2)
            num = num // 2
        for i in range(3, int(num**0.5) + 1, 2):
            while num % i == 0:
                factors.append(i)
                num = num // i
        if num > 2:
            factors.append(num)
        return factors

    # Print prime factors of numbers 1 to n
    for i in range(1, n + 1):
        print("%2d  (%s)" % (i, ", ".join(str(x) for x in prime_factors(i))))
    print()

    # Print multiplication table
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("%2d" % (i * j), end=" ")
        print()