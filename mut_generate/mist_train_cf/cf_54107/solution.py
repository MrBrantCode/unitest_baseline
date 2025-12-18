"""
QUESTION:
Create a function `will_it_fly(q, w, n, m, s)` that determines if a list of integers `q` can "fly" based on the following conditions: 
- the list `q` must be a palindrome
- the sum of its elements must be ≤ `w` maximum allowed weight
- consist of exactly `n` smallest unique digits
- "q" has no more than `m` prime numbers
- and fewer or equal to `s` numbers divisible by 5.
Return `True` if `q` can fly, otherwise return `False`.
"""

def will_it_fly(q, w, n, m, s):
    if not(sum(q) <= w):
        return False
    if not (q == q[::-1]):
        return False
    if len(set(q)) != n:
        return False
    prime_count = sum(is_prime(num) for num in q)
    if prime_count > m:
        return False
    divisible_by_5 = sum(num%5==0 for num in q)
    if divisible_by_5 > s:
        return False
    return True

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