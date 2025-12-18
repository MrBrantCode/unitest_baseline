"""
QUESTION:
Consider the range `0` to `10`. The primes in this range are: `2, 3, 5, 7`, and thus the prime pairs are: `(2,2), (2,3), (2,5), (2,7), (3,3), (3,5), (3,7),(5,5), (5,7), (7,7)`.

Let's take one pair `(2,7)` as an example and get the product, then sum the digits of the result as follows:  `2 * 7 = 14`, and `1 + 4 = 5`. We see that `5` is a prime number. Similarly, for the pair `(7,7)`, we get: `7 * 7 = 49`, and `4 + 9 = 13`, which is a prime number. 

You will be given a range and your task is to return the number of pairs that revert to prime as shown above. In the range `(0,10)`, there are only `4` prime pairs that end up being primes in a similar way: `(2,7), (3,7), (5,5), (7,7)`. Therefore, `solve(0,10) = 4)`

Note that the upperbound of the range will not exceed `10000`. A range of `(0,10)` means that: `0 <= n < 10`.

Good luck!

If you like this Kata, please try 

[Simple Prime Streaming](https://www.codewars.com/kata/5a908da30025e995880000e3)

[Prime reduction](https://www.codewars.com/kata/59aa6567485a4d03ff0000ca)

[Dominant primes](https://www.codewars.com/kata/59ce11ea9f0cbc8a390000ed)
"""

import itertools

def count_prime_pairs_reverting_to_prime(start, end):
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
            i += 6
        return True

    def sum_of_digits(n):
        return sum(map(int, str(n)))

    primes = set([2] + [n for n in range(3, end, 2) if is_prime(n)])
    prime_pairs = itertools.combinations_with_replacement([p for p in primes if start <= p < end], 2)
    
    count = 0
    for x, y in prime_pairs:
        product = x * y
        digit_sum = sum_of_digits(product)
        if is_prime(digit_sum):
            count += 1
    
    return count