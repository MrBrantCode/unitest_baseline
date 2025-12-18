"""
QUESTION:
Create a function called `last_prime_sum` that takes a list of integers as input, finds the last prime number in the list, and returns the product of its digits. The function should return the product as an integer.
"""

def last_prime_sum(lst):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    prime = None 
    for num in reversed(lst):
        if is_prime(num):
            prime = num
            break
    if prime is not None:
        return eval('*'.join(str(prime)))
    else:
        return None