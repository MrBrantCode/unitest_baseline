"""
QUESTION:
Create a function `is_prime` that accepts an array of integers and returns an array of booleans representing whether each corresponding integer is a prime number. The function must have a time complexity of O(n log(log n)).
"""

def is_prime(array):
    def sieve(n):
        sieve = [True] * (n+1)
        sieve[0:2] = [False, False] # 0 and 1 are not prime numbers
        for current_number in range(2, int(n**0.5)+1):
            if sieve[current_number]:
                for multiple in range(current_number*current_number, n+1, current_number):
                    sieve[multiple] = False
        return sieve

    maximum = max(array)
    primality_check = sieve(maximum)
    return [primality_check[i] for i in array]