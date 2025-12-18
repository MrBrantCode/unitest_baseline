"""
QUESTION:
Round any given number to the closest 0.5 step

I.E.
```
solution(4.2) = 4
solution(4.3) = 4.5
solution(4.6) = 4.5
solution(4.8) = 5
```

Round **up** if number is as close to previous and next 0.5 steps.

```
solution(4.75) == 5
```
"""

import math

def round_to_nearest_half(n: float) -> float:
    if n - 0.25 < math.floor(n):
        return math.floor(n)
    elif n - 0.75 < math.floor(n):
        return math.floor(n) + 0.5
    else:
        return math.ceil(n)