"""
QUESTION:
Develop a function named `calculate_parameters` that takes a list of numbers as input. The function should handle each number individually, determine if the quantity of factors is even, construct a list of these factors, calculate the sum of these factors, and identify the highest prime number among the factors. Additionally, the function should calculate the least common multiple (LCM) and the greatest common divisor (GCD) of the factors. If the LCM or GCD cannot be determined, the function should return a suitable message.

The function should be able to handle multiple inputs concurrently, returning a dictionary where the keys represent the input numbers and the values are tuples. Each tuple should include five elements: a boolean indicating if the quantity of factors is even, the list of factors, the sum of the factors, the highest prime number among the factors, and a tuple containing the LCM and GCD of the factors.

The function should only accept integer inputs. Non-integer inputs, including floating point numbers, should be converted to the nearest integer. String inputs should be converted to integers if possible. If the conversion is not possible, the function should return a suitable error message.
"""

from math import gcd 
from functools import reduce

def calculate_parameters(numbers):
    def LCM(a, b):
        return (a*b)//gcd(a,b)

    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors[-1]

    res = {}
    for n in numbers:
        try:
            n = float(n)
            if n.is_integer():
                n = int(n)
                factors = [x for x in range(1,n+1) if n%x==0]
                quantity = len(factors) % 2 == 0
                factors_sum = sum(factors)
                highest_prime = prime_factors(n)
                lcm = reduce(LCM, factors, 1)
                gcd_value = reduce(gcd, factors)
                res[n] = (quantity, factors, factors_sum, highest_prime, (lcm, gcd_value))
            else:
                continue
        except ValueError:
            print(f"Could not convert {n} to a float")
    return res