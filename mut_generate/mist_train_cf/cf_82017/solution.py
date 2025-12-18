"""
QUESTION:
Write a function named `multiplication_table_for_primes` that constructs a two-dimensional array containing a multiplication table for prime numbers exclusively between 0 and 50, and returns this table.
"""

def multiplication_table_for_primes(n):
    def prime_numbers(n):
        primes = []
        for possiblePrime in range(2, n + 1):
            isPrime = True
            for num in range(2, int(possiblePrime ** 0.5) + 1):
                if possiblePrime % num == 0:
                    isPrime = False
            if isPrime:
                primes.append(possiblePrime)
        return primes

    primes = prime_numbers(n)
    table = []
    for i in range(len(primes)):
        row = []
        for j in range(len(primes)):
            row.append(primes[i] * primes[j])
        table.append(row)
    return table