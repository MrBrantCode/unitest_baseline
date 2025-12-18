"""
QUESTION:
Create a function which checks a number for three different properties.

- is the number prime?
- is the number even?
- is the number a multiple of 10?

Each should return either true or false, which should be given as an array. Remark: The Haskell variant uses `data Property`.

### Examples
```python
number_property(7)  # ==> [true,  false, false] 
number_property(10) # ==> [false, true,  true] 
```
The number will always be an integer, either positive or negative. Note that negative numbers cannot be primes, but they can be multiples of 10:

```python
number_property(-7)  # ==> [false, false, false] 
number_property(-10) # ==> [false, true,  true] 
```
"""

import math

def number_property(n):
    return [is_prime(n), is_even(n), is_multiple_of_10(n)]

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def is_even(n):
    return n % 2 == 0

def is_multiple_of_10(n):
    return n % 10 == 0