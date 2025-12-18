"""
QUESTION:
You are given two positive integers ```a``` and ```b```.

You can perform the following operations on ```a``` so as to obtain ```b``` :
```
(a-1)/2   (if (a-1) is divisible by 2)
a/2       (if a is divisible by 2)
a*2
```
```b``` will always be a power of 2.

You are to write a function ```operation(a,b)``` that efficiently returns the minimum number of operations required to transform ```a``` into ```b```.

For example :
```
operation(2,8) -> 2
2*2 = 4
4*2 = 8

operation(9,2) -> 2
(9-1)/2 = 4
4/2 = 2

operation(1024,1024) -> 0
```
"""

from math import log2

def min_operations_to_transform(a, b):
    n = 0
    while log2(a) % 1 != 0:
        n += 1
        if (a - 1) % 2 == 0:
            a = (a - 1) // 2
        elif a % 2 == 0:
            a //= 2
        else:
            a *= 2
    return n + abs(int(log2(a)) - int(log2(b)))