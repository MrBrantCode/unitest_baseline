"""
QUESTION:
Every natural number, ```n```, may have a prime factorization like:



We define the **geometric derivative of n**, as a number with the following value:



For example: calculate the value of ```n*``` for ```n = 24500```.
```
24500 = 2²5³7²
n* = (2*2) * (3*5²) * (2*7) = 4200
```
Make a function, ```f``` that can perform this calculation
```
f(n) ----> n*
```
Every prime number will have ```n* = 1```.

Every number that does not have an exponent ```ki```, higher than 1, will give a ```n* = 1```, too

```python
f(24500) == 4200

f(997) == 1
```
Do your best!
"""

def geometric_derivative(n):
    res = 1
    i = 2
    while n != 1:
        k = 0
        while n % i == 0:
            k += 1
            n //= i
        if k != 0:
            res *= k * i ** (k - 1)
        i += 1
    return res