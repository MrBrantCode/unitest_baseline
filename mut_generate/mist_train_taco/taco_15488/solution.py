"""
QUESTION:
A strongness of an even number is the number of times we can successively divide by 2 until we reach an odd number starting with an even number n.

For example, if n = 12, then
* 12 / 2 = 6
* 6 / 2 = 3

So we divided successively 2 times and we reached 3, so the strongness of 12 is `2`.

If n = 16 then
* 16 / 2 = 8
* 8 / 2 = 4
* 4 / 2 = 2
* 2 / 2 = 1

we divided successively 4 times and we reached 1, so the strongness of 16 is `4`


# Task

Given a closed interval `[n, m]`, return the even number that is the strongest in the interval. If multiple solutions exist return the smallest strongest even number.

Note that programs must run within the allotted server time; a naive solution will probably time out.


# Constraints
```if-not:ruby
1 <= n < m <= INT_MAX
```
```if:ruby
1 <= n < m <= 2^64
```


# Examples
```
[1, 2]    -->   2  # 1 has strongness 0, 2 has strongness 1
[5, 10]   -->   8  # 5, 7, 9 have strongness 0; 6, 10 have strongness 1; 8 has strongness 3
[48, 56]  -->  48
"""

from math import log2

def find_strongest_even(n, m):
    # If the highest power of 2 within the interval is greater for m than for n,
    # then the strongest even number is the highest power of 2 within the interval.
    if int(log2(m)) > int(log2(n)):
        return 2 ** int(log2(m))
    
    # Adjust n and m to the nearest even numbers within the interval
    n += n % 2
    m -= m % 2
    
    # If n and m are the same after adjustment, return n
    if n == m:
        return n
    
    # Recursively find the strongest even number in the adjusted interval
    return 2 * find_strongest_even(n // 2, m // 2)