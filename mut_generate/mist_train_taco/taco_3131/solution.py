"""
QUESTION:
The sum of divisors of `6` is `12` and the sum of divisors of `28` is `56`. You will notice that `12/6 = 2` and `56/28 = 2`. We shall say that `(6,28)` is a pair with a ratio of `2`.  Similarly, `(30,140)` is also a pair but with a ratio of `2.4`. These ratios are simply decimal representations of fractions.

`(6,28)` and `(30,140)` are the only pairs in which `every member of a pair is 0 <= n < 200`. The sum of the lowest members of each pair is `6 + 30 = 36`. 

You will be given a `range(a,b)`, and your task is to group the numbers into pairs with the same ratios. You will return the sum of the lowest member of each pair in the range. If there are no pairs. return `nil` in Ruby, `0` in python. Upper limit is `2000`.

```Haskell
solve(0,200) = 36
```

Good luck!

if you like this Kata, please try:

[Simple division](https://www.codewars.com/kata/59ec2d112332430ce9000005)

[Sub-array division](https://www.codewars.com/kata/59eb64cba954273cd4000099)
"""

from collections import defaultdict
from fractions import Fraction
from bisect import bisect_left as bisect

# Precompute harmonic values and groups
harmonic = [0] + [Fraction(sum({y for x in range(1, int(n ** 0.5) + 1) for y in [x, n // x] if not n % x}), n) for n in range(1, 2001)]
harmonicity = defaultdict(set)
for (n, h) in enumerate(harmonic):
    harmonicity[h].add(n)

HARMO_GROUPS = {h: sorted(s) for (h, s) in harmonicity.items() if len(s) > 1}
HARMO_RATIOS = {n: h for (h, lst) in HARMO_GROUPS.items() for n in lst}
HARMO_NUM = sorted(HARMO_RATIOS.keys())

def sum_of_lowest_pairs_in_range(a, b):
    seens = set()
    s = 0
    n1, n2 = bisect(HARMO_NUM, a), bisect(HARMO_NUM, b)
    
    for n in HARMO_NUM[n1:n2]:
        if n not in seens:
            grp = [x for x in HARMO_GROUPS[HARMO_RATIOS[n]] if a <= x < b]
            if len(grp) > 1:
                seens |= set(grp)
                s += grp[0]
    
    return s