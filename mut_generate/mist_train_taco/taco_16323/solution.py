"""
QUESTION:
Get the next prime number!

You will get a number`n` (>= 0) and your task is to find the next prime number. 

Make sure to optimize your code: there will numbers tested up to about `10^12`.

## Examples

```
5   =>  7
12  =>  13
```
"""

from itertools import count

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for div in range(3, int(n ** 0.5) + 1, 2):
        if n % div == 0:
            return False
    return True

def find_next_prime(n):
    for candidate in count(n + 1):
        if is_prime(candidate):
            return candidate