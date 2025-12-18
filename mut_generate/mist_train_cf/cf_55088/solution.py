"""
QUESTION:
Create a function named `is_cube_of_sum_of_two_primes` that takes an integer `n` as input and returns a list of two prime numbers if `n` is a cube of the sum of those two prime numbers. If `n` does not meet this condition, return an empty list. The input integer `n` can go up to 1,000.
"""

def is_cube_of_sum_of_two_primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while(i * i <= num):
            if num%i == 0 or num%(i + 2) == 0:
                return False
            i = i + 6
        return True

    def is_cube(number):
        return round(number ** (1 / 3)) ** 3 == number

    if not is_cube(n):
        return []
    target = int(round(n ** (1 / 3)))
    primes = [i for i in range(2, target+1) if is_prime(i)]
    for i, prime1 in enumerate(primes):
        for prime2 in primes[i:]:
            if prime1 + prime2 == target:
                return [prime1, prime2]
    return []