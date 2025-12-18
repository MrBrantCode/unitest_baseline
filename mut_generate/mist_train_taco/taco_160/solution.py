"""
QUESTION:
Given an array of numbers, return an array, with each member of input array rounded to a nearest number, divisible by 5.

For example:
```
roundToFive([34.5, 56.2, 11, 13]);
```
should return
```
[35, 55, 10, 15]
```

```if:python
Roundings have to be done like "in real life": `22.5 -> 25`
```
"""

from decimal import Decimal, ROUND_HALF_UP

def round_to_nearest_five(numbers):
    return [(n / 5).quantize(1, ROUND_HALF_UP) * 5 for n in map(Decimal, numbers)]