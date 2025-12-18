"""
QUESTION:
Write a function `max_prime_sum(lst)` that takes a list of integers as input and returns the maximum sum of digits of a prime number in the list. 

The function should handle large lists and return 0 if no prime number is found in the list. There are no restrictions on the size of the input list or the range of integers in the list.
"""

def max_prime_sum(lst):
    def is_prime(n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n<9: return True
        if n%3 == 0: return False
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n%f == 0: return False
            if n%(f+2) == 0: return False
            f +=6
        return True     
            
    def sum_of_digits(n):
        return sum(int(digit) for digit in str(n))

    primes = (i for i in lst if is_prime(i))
    return max((sum_of_digits(prime) for prime in primes), default=0)