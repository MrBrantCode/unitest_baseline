"""
QUESTION:
Consider the number `1176` and its square (`1176 * 1176) = 1382976`. Notice that:

* the first two digits of `1176` form a prime.
* the first two digits of the square `1382976` also form a prime.
* the last two digits of `1176` and `1382976` are the same. 

Given two numbers representing a range (`a, b`), how many numbers satisfy this property within that range? (`a <= n < b`)


## Example

`solve(2, 1200) = 1`, because only `1176` satisfies this property within the range `2 <= n < 1200`. See test cases for more examples. The upper bound for the range will not exceed `1,000,000`. 

Good luck!

If you like this Kata, please try:

[Simple Prime Streaming](https://www.codewars.com/kata/5a908da30025e995880000e3)

[Alphabet symmetry](https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0)

[Upside down numbers](https://www.codewars.com/kata/59f7597716049833200001eb)
"""

def count_special_numbers(a, b):
    # List of two-digit prime numbers
    prime_prefixes = ['11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97']
    
    count = 0
    for i in range(a, b):
        if (i * i - i) % 100 == 0 and str(i)[:2] in prime_prefixes and str(i * i)[:2] in prime_prefixes:
            count += 1
    
    return count