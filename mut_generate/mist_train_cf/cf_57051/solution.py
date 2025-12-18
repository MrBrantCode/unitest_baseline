"""
QUESTION:
Create a function `product_of_distinct_prime_factors` that takes a list of numbers as input and returns a list where each element is the product of distinct prime factors of the corresponding number in the input list. The function should be optimized to handle large input lists efficiently.
"""

def product_of_distinct_prime_factors(numbers):
    import math
    def prime_factors(n):
        # This function finds out prime factors
        factors = set()
        while n % 2 == 0:
            factors.add(2),
            n /= 2
        for i in range(3, int(math.sqrt(n))+1, 2):
            while n % i== 0:
                factors.add(i),
                n /= i
        if n > 2:
            factors.add(n)
        return factors

    res = []
    for number in numbers:
        factors = prime_factors(number)
        product = 1
        for factor in factors:
            product *= factor
        res.append(product)
    return res