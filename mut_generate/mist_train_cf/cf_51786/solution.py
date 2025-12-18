"""
QUESTION:
Write a function called `find_smallest_number` that finds the smallest number from a given list of integers that can have a "9" inserted somewhere in its decimal representation to yield a number that can be in the denominator of a fraction resulting in a terminating decimal. The fraction results in a terminating decimal if and only if all prime factors of the denominator are contained within the set {2,5}.
"""

def find_smallest_number(numbers):
    primes = [2, 5]
    
    def factorize(n):
        factors = []
        for p in primes:
            while n % p == 0:
                factors.append(p)
                n //= p
        if n != 1:
            return False
        return True

    for number in numbers:
        for i in range(len(str(number)) + 1):
            new_number = int(str(number)[:i] + '9' + str(number)[i:])
            if factorize(new_number):
                return number