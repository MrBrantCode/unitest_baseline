"""
QUESTION:
Write a function called `prime_sum_product` that takes two integers `a` and `b` as input, representing a range of numbers [a, b], and returns a tuple containing the sum and product of all prime numbers within that range. Assume that `a` is less than or equal to `b`.
"""

def prime_sum_product(a, b):
    prime_sum = 0
    prime_product = 1
    
    for num in range(a, b+1):
        if num < 2:
            continue
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            prime_sum += num
            prime_product *= num
    
    return prime_sum, prime_product