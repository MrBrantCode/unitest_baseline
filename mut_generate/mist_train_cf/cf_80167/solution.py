"""
QUESTION:
Write two functions, `product_of_primes(N)` and `sum_of_composites(nums)`, where `product_of_primes(N)` calculates the product of the first N prime numbers and `sum_of_composites(nums)` calculates the sum of all composite numbers in the list `nums`. Assume that `nums` contains only natural numbers and `N` is a positive integer.
"""

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

def product_of_primes(N):  
    primes_prod = 1  
    count = 0  
    num = 2  
    
    while count < N:
        if is_prime(num):
            primes_prod *= num
            count += 1
        num += 1

    return primes_prod

def sum_of_composites(nums):  
    composite_sum = 0  
    
    for num in nums:
        if num > 1 and not is_prime(num):
            composite_sum += num

    return composite_sum