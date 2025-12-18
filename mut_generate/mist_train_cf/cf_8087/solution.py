"""
QUESTION:
Write a function `generate_array(n, m)` that generates an array of increasing numbers from 1 to m, where each number in the array must be divisible by a prime number less than or equal to n, and the array must contain at least n/2 prime numbers.
"""

def generate_array(n, m):
    primes = [2]  # Start with the first prime number
    result = []
    num = 1

    while len(result) < m:
        divisible_by_prime = False

        for prime in primes:
            if num % prime == 0:
                divisible_by_prime = True
                break

        if divisible_by_prime:
            result.append(num)
        else:
            for i in range(primes[-1] + 1, num + 1):
                is_prime = True
                for prime in primes:
                    if i % prime == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(i)

        num += 1

    return result[:m]