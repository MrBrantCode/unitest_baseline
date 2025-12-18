"""
QUESTION:
Create a function named `atmospheric_ascent` that takes four parameters: `q` (a list of numbers), `w`, `n`, and `p`. The function should return `True` if the following conditions are met:
- The sum of all numbers in list `q` is less than or equal to `w`.
- The list `q` is a palindrome, meaning it reads the same forwards and backwards when converted to a string.
- The number of distinct numbers in `q` is equal to `n`.
- The number of prime numbers in `q` is less than or equal to `p`.
Otherwise, the function should return `False`.

The function should contain two helper functions: `is_palindrome` to check if a given list is a palindrome, and `is_prime` to check if a given number is prime. 

Restrictions: The input list `q` contains only positive integers.
"""

def atmospheric_ascent(q, w, n, p):
    def is_palindrome(lst):
        return str(lst) == str(lst)[::-1]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    sum_q = sum(q)
    distinct_num_nums = len(set(q))
    prime_count = sum(1 for i in q if is_prime(i))

    return sum_q <= w and is_palindrome(q) and distinct_num_nums == n and prime_count <= p