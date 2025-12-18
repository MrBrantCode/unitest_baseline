"""
QUESTION:
Create a function `required_sequence(n)` that generates a sequence of distinct prime numbers where each successive prime number is greater than the triple of its preceding prime number, given an upper limit `n`. The sequence should be as long as possible.
"""

def required_sequence(n):
    def generate_primes(n):
        primes = []
        candidates = list(range(2, n+1))

        while len(candidates) != 0:
            prime = candidates[0]
            primes.append(prime)
            candidates = [x for x in candidates if x % prime != 0]

        return primes

    primes = generate_primes(n)
    result = []
    for prime in primes:
        if len(result) == 0 or prime > 3 * result[-1]:
            result.append(prime)
    return result