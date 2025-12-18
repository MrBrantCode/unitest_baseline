"""
QUESTION:
Define a function that takes one integer argument and returns logical value `true` or `false` depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

## Requirements

* You can assume you will be given an integer input.
* You can not assume that the integer will be only positive. You may be given negative numbers as well (or `0`).
* **NOTE on performance**: There are no fancy optimizations required, but still *the* most trivial solutions might time out. Numbers go up to 2^31 (or similar, depends on language version). Looping all the way up to `n`, or `n/2`, will be too slow.

## Example
```nasm    
mov edi, 1
call is_prime    ; EAX <- 0 (false)

mov edi, 2
call is_prime    ; EAX <- 1 (true)

mov edi, -1
call is_prime    ; EAX <- 0 (false)
```
"""

import random

def even_odd(n):
    (s, d) = (0, n)
    while d % 2 == 0:
        s += 1
        d >>= 1
    return (s, d)

def Miller_Rabin(a, p):
    (s, d) = even_odd(p - 1)
    a = pow(a, d, p)
    if a == 1:
        return True
    for i in range(s):
        if a == p - 1:
            return True
        a = pow(a, 2, p)
    return False

def is_prime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    return all((Miller_Rabin(random.randint(2, n - 1), n) for _ in range(40)))