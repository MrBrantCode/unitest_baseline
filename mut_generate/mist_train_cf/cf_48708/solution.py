"""
QUESTION:
Implement two functions, `is_prime` and `will_it_fly`. The `is_prime` function should take an integer `n` and return `True` if it's prime, `False` otherwise. The `will_it_fly` function should take a list of integers `q` and four integers `w`, `n`, `m`, and `s` as input. It should return `True` if the following conditions are met: 
1) The sum of the elements in `q` is less than or equal to `w`.
2) The list `q` is a palindrome.
3) The number of unique elements in `q` is equal to `n`.
4) The number of prime numbers in `q` is less than or equal to `m`.
5) The number of elements in `q` divisible by 5 is less than or equal to `s`. Otherwise, return `False`.
"""

def is_prime(n): 
    if n <= 1: 
        return False 
    if n <= 3: 
        return True 
    if n % 2 == 0 or n % 3 == 0: 
        return False 
    i = 5 
    while i * i <= n: 
        if n % i == 0 or n % (i + 2) == 0: 
            return False 
        i = i + 6 
    return True 

def will_it_fly(q, w, n, m, s): 
    if not(sum(q) <= w): 
        return False 
    if not(q == q[::-1]): 
        return False 
    if len(set(q)) != n: 
        return False 
    prime_count = sum(is_prime(num) for num in q) 
    if prime_count > m: 
        return False 
    divisible_by_5 = sum(num % 5 == 0 for num in q) 
    if divisible_by_5 > s: 
        return False 
    return True 