"""
QUESTION:
Write a function `generate_array(n, m)` where `n` is a positive integer and `m` is a positive integer greater than or equal to `n/2`. The function should generate an array of increasing numbers beginning from 1 and ending at `m`, where each number in the array is divisible by a prime number less than or equal to `n`, and the array contains exactly `k` prime numbers, where `k` is a positive integer greater than or equal to `n/2`.
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