"""
QUESTION:
The task is simply stated. Given an integer n (3 < n < 10^(9)), find the length of the smallest list of [*perfect squares*](https://en.wikipedia.org/wiki/Square_number) which add up to n. Come up with the best algorithm you can; you'll need it!

Examples:

sum_of_squares(17) = 2  17 = 16 + 1 (4 and 1 are perfect squares).
sum_of_squares(15) = 4  15 = 9 + 4 + 1 + 1. There is no way to represent 15 as the sum of three perfect squares.
sum_of_squares(16) = 1  16 itself is a perfect square.

Time constraints:

5 easy (sample) test cases: n < 20

5 harder test cases: 1000 < n < 15000

5 maximally hard test cases: 5 * 1e8 < n < 1e9

```if:java
300 random maximally hard test cases: 1e8 < n < 1e9
```
```if:c#
350 random maximally hard test cases: 1e8 < n < 1e9
```
```if:python
15 random maximally hard test cases: 1e8 < n < 1e9
```
```if:ruby
25  random maximally hard test cases: 1e8 < n < 1e9
```
```if:javascript
100 random maximally hard test cases: 1e8 < n < 1e9
```
```if:crystal
250 random maximally hard test cases: 1e8 < n < 1e9
```
```if:cpp
Random maximally hard test cases: 1e8 < n < 1e9
```
"""

def sum_of_squares(n: int) -> int:
    def one_square(n):
        return round(n ** 0.5) ** 2 == n

    def two_squares(n):
        while n % 2 == 0:
            n //= 2
        p = 3
        while p * p <= n:
            while n % (p * p) == 0:
                n //= p * p
            while n % p == 0:
                if p % 4 == 3:
                    return False
                n //= p
            p += 2
        return n % 4 == 1

    def three_squares(n):
        while n % 4 == 0:
            n //= 4
        return n % 8 != 7

    if one_square(n):
        return 1
    if two_squares(n):
        return 2
    if three_squares(n):
        return 3
    return 4