"""
QUESTION:
Create a function that finds the largest palindromic number made from the product of **at least 2** of the given arguments.

### Notes

* Only non-negative numbers will be given in the argument
* You don't need to use all the digits of the products
* Single digit numbers are considered palindromes
* Optimization is needed: dealing with ones and zeros in a smart way will help a lot




## Examples

```
[937, 113] --> 81518
```
As `937 * 113 = 105881` and the largest palindromic number that can be arranged from the digits of result is: `81518`


Another one:

```
[57, 62, 23] --> 82128

             product     palindrome
57 * 62      = 3534   -->  353
57 * 23      = 1311   -->  131
62 * 23      = 1426   -->  6
57 * 62 * 23 = 81282  -->  82128
```

One more:
```
[15, 125, 8] --> 8

             product     palindrome
15 * 125     = 1875   -->  8
15 * 8       = 120    -->  2
125 * 8      = 1000   -->  1
15 * 125 * 8 = 15000  -->  5
```
"""

from collections import Counter
from itertools import combinations
from operator import mul
from functools import reduce

def largest_palindrom_from(n):
    digits = sorted(str(n))
    singles, pairs = [], []
    while digits:
        digit = digits.pop()
        if digits and digit == digits[-1]:
            pairs.append(digit)
            digits.pop()
        else:
            singles.append(digit)
    if pairs and pairs[0] == '0':
        pairs = []
    if not singles:
        singles = ['']
    return int(''.join(pairs) + singles[0] + ''.join(pairs[::-1]))

def find_largest_palindromic_product(*args):
    args = Counter(args)
    candidates = set()
    for n in [0, 1]:
        if args[n] > 2:
            args[n] = 2
    args = list(args.elements())
    for n in range(2, len(args) + 1):
        for combo in combinations(args, n):
            product = reduce(mul, combo)
            candidates.add(largest_palindrom_from(product))
    return max(candidates)