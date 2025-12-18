"""
QUESTION:
Consider the prime number `23`. If we sum the square of its digits we get:
`2^2 + 3^2 = 13`, then for `13: 1^2 + 3^2 = 10`, and finally for `10: 1^2 + 0^2 = 1`. 

Similarly, if we start with prime number `7`, the sequence is: `7->49->97->130->10->1`.

Given a range, how many primes within that range will eventually end up being `1`? 

The upperbound for the range is `50,000`. A range of `(2,25)` means that: `2 <= n < 25`. 

Good luck!

If you like this Kata, please try:

[Prime reversion](https://www.codewars.com/kata/59b46276afcda204ed000094)

[Domainant primes](https://www.codewars.com/kata/59ce11ea9f0cbc8a390000ed)
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqrtn = int(n ** 0.5) + 1
    for i in range(5, sqrtn, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def end_one(n):
    while n > 6:
        n = sum(map(lambda x: int(x) * int(x), f'{n}'))
        if n == 1:
            return True
    return False

def count_primes_ending_in_one(start, end):
    return sum((1 for n in range(start, end) if is_prime(n) and end_one(n)))