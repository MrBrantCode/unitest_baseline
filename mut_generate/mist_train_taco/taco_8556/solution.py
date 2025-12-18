"""
QUESTION:
An integral:
  


can be approximated by the so-called Simpson’s rule:




Here `h = (b-a)/n`, `n` being an even integer and `a <= b`. 

We want to try Simpson's rule with the function f:



The task is to write a function called `simpson` with parameter `n` which returns the value of the integral of f on the interval `[0, pi]` (pi being 3.14159265359...).
## Notes:
- Don't round or truncate your results. See in "RUN EXAMPLES" the function `assertFuzzyEquals` or `testing`.
- `n` will always be even.

- We know that the exact value of the integral of f on the given interval is `2`.

You can see: 
about rectangle method and trapezoidal rule.
"""

def simpson(n, a=0, b=3.14159265359, f=lambda x: 3 / 2 * sin(x) ** 3):
    from math import sin, pi
    h = (b - a) / n
    integral = 0
    integral += f(a) + f(b)
    integral += 4 * sum((f(a + (2 * i - 1) * h) for i in range(1, n // 2 + 1)))
    integral += 2 * sum((f(a + 2 * i * h) for i in range(1, n // 2)))
    integral *= h / 3
    return integral