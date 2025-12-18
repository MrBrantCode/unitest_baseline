"""
QUESTION:
Create a function `smallest_prime` that takes a list of integers as input and returns the smallest prime number in the list. The function should return the smallest prime number. If no prime numbers exist in the list, the function's behavior is undefined. Assume the input list contains at least one prime number.
"""

def smallest_prime(numbers):
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))
    
    primes = [num for num in numbers if is_prime(num)]
    return min(primes)