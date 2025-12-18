"""
QUESTION:
Write a function that prints a list of prime numbers from 0 to the given limit that are divisible by both 2 and 3. The function should only use a single loop and must not make use of the modulo operator.
"""

def entrance(limit):
    def is_prime(num):
        if num < 2:
            return False
        if num < 4:
            return True
        if (num & 1 == 0) or (num & (num - 1) == num - 1 and num != 3):
            return False
        
        divisor = 5
        while divisor * divisor <= num:
            if (num & divisor == 0) or (num & (divisor + 2) == 0):
                return False
            divisor += 6
        
        return True

    primes = []
    for num in range(0, limit + 1, 6):
        if is_prime(num + 2):
            primes.append(num + 2)
        if is_prime(num + 4):
            primes.append(num + 4)
    print(primes)