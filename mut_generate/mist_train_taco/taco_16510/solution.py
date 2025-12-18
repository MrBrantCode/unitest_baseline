"""
QUESTION:
In this Kata, you will be given two positive integers `a` and `b` and your task will be to apply the following operations:

```
i) If a = 0 or b = 0, return [a,b]. Otherwise, go to step (ii);
ii) If a ≥ 2*b, set a = a - 2*b, and repeat step (i). Otherwise, go to step (iii);
iii) If b ≥ 2*a, set b = b - 2*a, and repeat step (i). Otherwise, return [a,b].
```

`a` and `b` will both be lower than 10E8.

More examples in tests cases. Good luck!

Please also try [Simple time difference](https://www.codewars.com/kata/5b76a34ff71e5de9db0000f2)
"""

def reduce_integers(a: int, b: int) -> list:
    if not (a and b):
        return [a, b]
    if a >= 2 * b:
        return reduce_integers(a % (2 * b), b)
    if b >= 2 * a:
        return reduce_integers(a, b % (2 * a))
    return [a, b]