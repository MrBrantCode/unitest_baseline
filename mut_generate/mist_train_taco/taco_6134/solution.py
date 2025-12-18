"""
QUESTION:
Consider the numbers `6969` and `9116`. When you rotate them `180 degrees` (upside down), these numbers remain the same. To clarify, if we write them down on a paper and turn the paper upside down, the numbers will be the same. Try it and see! Some numbers such as `2` or `5` don't yield numbers when rotated.

Given a range, return the count of upside down numbers within that range.  For example, `solve(0,10) = 3`, because there are only `3` upside down numbers `>= 0 and < 10`. They are `0, 1, 8`.

More examples in the test cases.

Good luck!

If you like this Kata, please try 

[Simple Prime Streaming](https://www.codewars.com/kata/5a908da30025e995880000e3)

[Life without primes](https://www.codewars.com/kata/59f8750ac374cba8f0000033)

Please also try the performance version of this kata at [Upside down numbers - Challenge Edition ](https://www.codewars.com/kata/59f98052120be4abfa000304)
"""

def count_upside_down_numbers(start, end):
    REV = {'6': '9', '9': '6'}
    BASE = set('01869')

    def is_reversible(n):
        s = str(n)
        return not set(s) - BASE and (not len(s) % 2 or s[len(s) // 2] not in '69') and all((REV.get(c, c) == s[-1 - i] for (i, c) in enumerate(s[:len(s) // 2])))

    return sum((is_reversible(n) for n in range(start, end)))