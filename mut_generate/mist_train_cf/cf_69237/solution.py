"""
QUESTION:
Write a function `intricate_prime_triplet_product(a)` that determines if a given number `a` is the product of three distinct prime numbers and returns the triplet of primes if found. The function should accept `a` as input, where `0 <= a <= 10000`, and return either a tuple of three distinct prime numbers or the message 'Not a product of 3 distinct prime numbers.' The function should implement a prime number generator and a divide and conquer approach to find the prime triplet.
"""

def intricate_prime_triplet_product(a):
    if a > 10000 or a < 0:
        raise Exception('a should be between 0 and 10000')

    def prime_generator(n):
        prime_list = [True for _ in range(n+1)]
        p = 2
        while p**2 <= n:
            if prime_list[p] == True:
                yield p
                for i in range(p**2, n+1, p):
                    prime_list[i] = False
            p += 1

    def find_triplet_product(primes, target):
        primes.sort()
        n = len(primes)
        for i in range(0, n-3):
            if i != 0 and primes[i] == primes[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                sum = primes[i] * primes[j] * primes[k]
                if sum == target:
                    return (primes[i], primes[j], primes[k])
                elif sum < target:
                    j += 1
                else:
                    k -= 1
        return ('Not a product of 3 distinct prime numbers.')

    primes = [p for p in prime_generator(a)]
    return(find_triplet_product(primes, a))