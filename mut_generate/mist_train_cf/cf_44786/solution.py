"""
QUESTION:
Write a function `find_primes_and_factors(nums)` that accepts a list of integers `nums` and returns a dictionary where the keys are the prime numbers from the list and the values are the number of distinct prime factors for each prime number. The function should optimize primality testing for large input values.
"""

def find_primes_and_factors(nums):
    def is_prime(num):
        if num == 1:
            return False
        elif num == 2:
            return True
        elif num > 2 and num % 2 == 0:
            return False
        else:
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True

    def prime_factors(num):
        factors_set = set()
        while num % 2 == 0:
            factors_set.add(2),
            num = num / 2
        for i in range(3,int(num**0.5)+1,2):
            while num % i== 0:
                factors_set.add(i),
                num = num / i
        if num > 2:
            factors_set.add(num)
        return len(factors_set)

    prime_dict = {}
    for num in nums:
        if is_prime(num):
            prime_dict[num] = prime_factors(num)
    return prime_dict