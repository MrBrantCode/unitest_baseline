"""
QUESTION:
Create a function named `calculate_x` that takes three integer parameters `a`, `b`, and `c`. The function should perform the following operations:
- Add `a` and `b` and assign the result to `a`.
- Multiply `a` and `c` and assign the result to `a`.
- Subtract `b` from `a` and assign the result to `a`.
- Check if `a` is divisible by `c`. If it is, subtract `c` from `a`.
- Return the final value of `a`.
"""

def calculate_x(a, b, c):
    a += b
    a *= c
    a -= b
    if a % c == 0:
        a -= c
    return a