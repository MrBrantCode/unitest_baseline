"""
QUESTION:
Create a function called `multiplication_table(n)` that prints a multiplication table of all prime numbers less than or equal to `n`. The table should be formatted with the prime numbers along the top row and the products of the prime numbers in the corresponding cells. The function should only print the table, without returning any value. The input `n` is an integer.
"""

def multiplication_table(n):
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    primes = [x for x in range(2, n + 1) if is_prime(x)]
    print("Multiplication Table for Prime Numbers up to", n)
    print("\t" + "\t".join(map(str, primes)))  # print header row
    for i in primes:
        row = [str(i*j) for j in primes]
        print(str(i) + "\t" + "\t".join(row))  # print each row with prime number