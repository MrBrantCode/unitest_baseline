"""
QUESTION:
Write a function `locate_numbers` that takes a list of integers as input. The function should return a tuple `(a, b, c, d, e, f)` where `a` and `b` are the smallest and largest prime numbers in the list, respectively, and `c` and `d` are the smallest and largest composite numbers in the list, respectively. The function should also return the sum of all prime numbers (`e`) and the sum of all composite numbers (`f`) in the list. If a condition (smallest/largest prime/composite or their sum) is not satisfied (i.e., if there are no prime or composite numbers in the list), the corresponding value in the tuple should be `None`.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def locate_numbers(lst):
    primes = [i for i in lst if is_prime(i)]
    composites = [i for i in lst if not is_prime(i) and i>1] # excluding 1 as it's neither prime nor composite

    a, b, e = min(primes) if primes else None, max(primes) if primes else None, sum(primes) if primes else None
    c, d, f = min(composites) if composites else None, max(composites) if composites else None, sum(composites) if composites else None

    return a, b, c, d, e, f