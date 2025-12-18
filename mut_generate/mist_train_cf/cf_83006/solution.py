"""
QUESTION:
Implement a function `identify_primes` that takes two arguments: `lower` and `upper` bounds of a range (both inclusive). The function should iterate through this range, verifying the primality of each number and storing it along with relevant data. Each prime number should be accompanied by a statement that it is indeed prime, and each number found to be not prime should be reported along with its smallest prime divisor. The function should minimize computational time by using an efficient algorithm to check primality.
"""

def identify_primes(lower, upper):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return i
        return True

    for num in range(lower, upper + 1):
        check = is_prime(num)
        if check == True:
            print(f'{num} is a prime number')
        else:
            print(f'{num} is not a prime number, its smallest prime divisor is {check}')