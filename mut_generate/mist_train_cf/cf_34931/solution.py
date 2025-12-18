"""
QUESTION:
Create a Python function called `formula` that takes five integer parameters `a`, `b`, `c`, `d`, and `e`. Calculate two intermediate terms, `termino1` and `termino2`, where `termino1` is the sum of the factorials of `a`, `b`, and `c` divided by the factorial of `d`, and `termino2` is `e` raised to the power of `c` divided by the factorial of `e`. The function should return the sum of `termino1` and `termino2` rounded to two decimal places.
"""

def formula(a, b, c, d, e):
    def factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
    
    termino1 = (factorial(a) + factorial(b) + factorial(c)) / factorial(d)
    termino2 = pow(e, c) / factorial(e)
    result = termino1 + termino2
    return round(result, 2)