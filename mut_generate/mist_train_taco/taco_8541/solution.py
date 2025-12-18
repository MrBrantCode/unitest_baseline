"""
QUESTION:
A factorial (of a large number) will usually contain some trailing zeros.
Your job is to make a function that calculates the number of trailing zeros, in any given base.

Factorial is defined like this:
```n! = 1 * 2 * 3 * 4 * ... * n-2 * n-1 * n```

Here's two examples to get you started:

```python
trailing_zeros(15, 10) == 3
#15! = 1307674368000, which has 3 zeros at the end

trailing_zeros(7, 2) == 4
#7! = 5030 = 0b1001110110000, which has 4 zeros at the end
```

Your code should be able to handle some very large numbers, so write some smart code.

Note: ```num``` will be a non-negative integer, ```base``` will be an integer larger or equal to two.

HINT: Should you not make any headway after trying a long time, you should try [this kata](https://www.codewars.com/kata/number-of-trailing-zeros-of-n) first.
"""

def count_trailing_zeros_in_factorial(n: int, base: int) -> int:
    def isqrt(num: int) -> int:
        (res, bit) = (0, 1)
        while bit <= num:
            bit <<= 2
        bit >>= 2
        while bit:
            if num >= res + bit:
                num -= res + bit
                res += bit << 1
            res >>= 1
            bit >>= 2
        return res

    def factorize(n: int) -> list:
        factors = []
        for q in (2, 3):
            m = 0
            while not n % q:
                m += 1
                n //= q
            if m:
                factors.append((q, m))
        (m, d, q, maxq) = (0, 4, 1, isqrt(n))
        while q <= maxq:
            (q, d) = (q + d, 6 - d)
            while not n % q:
                m += 1
                n //= q
            if m:
                factors.append((q, m))
                (m, d, q, maxq) = (0, 4, 1, isqrt(n))
        if n > 1:
            factors.append((n, 1))
        return factors

    def count_factor(n: int, f: int) -> int:
        s = 0
        while n >= f:
            n //= f
            s += n
        return s

    return min((count_factor(n, f) // m for (f, m) in factorize(base)))