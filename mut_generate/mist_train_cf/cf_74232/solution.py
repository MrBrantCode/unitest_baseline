"""
QUESTION:
Write a function named `categorize_2D` that categorizes elements of a 2D array into prime, non-prime numbers and composite numbers with more than two distinct prime factors. The function should return a dictionary with three keys ("Prime", "Non_prime", "Composite") where "Non_prime" is a dictionary with keys "Even" and "Odd", and the values are lists containing the numbers corresponding to each category. Consider negative numbers and zero as non-prime.
"""

import numpy as np

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= abs(n):
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return len(set(factors))

def categorize_2D(arr):
    res = {"Prime": [], "Non_prime": {"Even": [], "Odd": []}, "Composite": []}
    for row in arr:
        for num in row:
            if is_prime(num):
                res["Prime"].append(num)
            elif num > 1 and prime_factors(num) > 2:
                res["Composite"].append(num)
            else:
                if num % 2 == 0:
                    res["Non_prime"]["Even"].append(num)
                else:
                    res["Non_prime"]["Odd"].append(num)
    return res