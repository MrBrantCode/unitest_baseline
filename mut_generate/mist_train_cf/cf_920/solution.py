"""
QUESTION:
Create a function named `generate_primes` that takes two parameters `start` and `end` representing the range of numbers, and returns a list of all prime numbers within that range. The function should have a time complexity of O(n√m) and a space complexity of O(n), where n is the length of the range and m is the maximum value in the range. The function should not use any built-in prime number functions or libraries. It should also handle negative ranges, ranges with non-integer values, and large ranges efficiently without running out of memory or exceeding the time complexity.
"""

def generate_primes(start, end):
    primes = []

    start = int(start)
    end = int(end)

    for possiblePrime in range(start, end + 1):
        isPrime = True

        if possiblePrime < 2:
            continue

        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(possiblePrime)

    return primes