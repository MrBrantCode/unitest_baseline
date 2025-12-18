"""
QUESTION:
The function `intricate_prime_triplet_product` takes an integer `a` as input, where `0 <= a <= 10000`. It should return a tuple of three distinct prime numbers whose product equals `a`, or a message indicating that no such triplet exists.
"""

def intricate_prime_triplet_product(a):
    if a > 10000 or a < 0:
        raise Exception('a should be between 0 and 10000')

    def generate_prime_numbers(n):
        prime_numbers = [True for _ in range(n + 1)]
        p = 2
        while p**2 <= n:
            if prime_numbers[p] == True:
                for i in range(p**2, n+1, p):
                    prime_numbers[i] = False
            p += 1
        return [p for p in range(2, n+1) if prime_numbers[p]]

    def find_triplet_product(primes, target):
        primes.sort()
        n = len(primes)
        for i in range(0, n-3):
            if i != 0 and primes[i] == primes[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                product = primes[i] * primes[j] * primes[k]
                if product == target:
                    return (primes[i], primes[j], primes[k])
                elif product < target:
                    j += 1
                else:
                    k -= 1
        return 'Not a product of 3 distinct prime numbers.'

    primes = generate_prime_numbers(a)
    return find_triplet_product(primes, a)