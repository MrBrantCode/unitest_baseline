"""
QUESTION:
Let us define a function `f`such as:

- (1) for k positive odd integer > 2 : 



- (2) for k positive even integer >= 2 : 



- (3) for k positive integer > 1 : 




where `|x|` is `abs(x)` and Bk the kth Bernoulli number.

`f` is not defined for `0, 1, -1`. These values will not be tested.

# Guidelines for Bernoulli numbers:

https://en.wikipedia.org/wiki/Bernoulli_number

http://mathworld.wolfram.com/BernoulliNumber.html

https://www.codewars.com/kata/bernoulli-numbers-1

There is more than one way to calculate them. You can make Pascal triangle and then with the basic formula below generate all Bernoulli numbers.

1 + 2B1 = 0 ... gives ...
  B1 = - 1/2

1 + 3B1 + 3B2 = 0 ... gives ...    B2        = 1/6

1 + 4B1 + 6B2 + 4B3 = 0 ... gives ... B3 = 0

1 + 5B1 + 10B2 + 10B3 + 5B4 = 0 ... gives ... B4 = - 1/30

... and so on


# Task 

Function `series(k, nb)` returns (1), (2) or (3) where `k` is the `k` parameter of `f` and `nb` the upper bound in the summation of (1). `nb` is of no use for (2) and (3) but for the sake of simplicity it will always appear in the tests even for cases (2) and (3) with a value of `0`.

```
Examples
S(2, 0) = 1.644934066848224....
S(3, 100000) = 1.20205690310973....
S(4, 0) = 1.08232323371113.....
S(-5, 0) = -0.003968253968....
S(-11, 0) = 0.02109279609279....
```

# Notes

- For Java, C#, C++: `k` should be such as `-27 <= k <= 20`; otherwise `-30 <= k <= 30` and be careful of 32-bit integer overflow.
- Translators are welcome.
"""

from math import factorial, pi
from fractions import Fraction

def comb(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))

def bernoulli(m):
    b = [1]
    for i in range(1, m + 1):
        n = 0
        for k in range(0, i):
            n += comb(i + 1, k) * b[k]
        b.append(Fraction(-n, i + 1))
    return b

# Precompute Bernoulli numbers up to 31
b = bernoulli(31)

def calculate_series(k, nb):
    if k < 0:
        k = -k
        return float(b[k + 1] * (-1) ** k / (k + 1))
    elif k % 2 == 1:
        return sum((1 / n ** k for n in range(1, nb + 1)))
    else:
        return float(abs(b[k]) * (2 * pi) ** k / (2 * factorial(k)))