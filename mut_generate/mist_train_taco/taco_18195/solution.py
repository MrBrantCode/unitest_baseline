"""
QUESTION:
# Task

Find the integer from `a` to `b` (included) with the greatest number of divisors. For example:

```
divNum(15, 30)   ==> 24
divNum(1, 2)     ==> 2
divNum(0, 0)     ==> 0
divNum(52, 156)  ==> 120
```

If there are several numbers that have the same (maximum) number of divisors, the smallest among them should be returned. Return the string `"Error"` if `a > b`.
"""

import numpy as np

# Precompute the number of divisors for each number up to 100000
s = np.ones(100000)
for i in range(2, 100000):
    s[i::i] += 1

def find_max_divisors_in_range(a, b):
    if a > b:
        return "Error"
    return max(range(a, b + 1), key=lambda i: (s[i], -i), default='Error')