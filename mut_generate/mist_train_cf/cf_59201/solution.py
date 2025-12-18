"""
QUESTION:
Create a function `extract_primes` that takes a list of integers as input and returns a tuple containing a list of all prime numbers from the input list and their sum. The input list can contain duplicates and negative numbers.
"""

def extract_primes(nums):
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    prime_nums = [num for num in nums if is_prime(num)]
    return prime_nums, sum(prime_nums)