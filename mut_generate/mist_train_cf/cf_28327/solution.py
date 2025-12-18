"""
QUESTION:
Implement the `return_point` function that takes three parameters: `m` (integer), `npts` (integer), and `k` (integer). The function returns a floating-point value based on the following rules: 
- If `k` is 1, the function returns `m / npts`
- If `k` is 2, the function returns `sin(2 * pi * m / npts)`
- If `k` is 3, the function returns `cos(2 * pi * m / npts)`
- If `k` is 4, the function returns `tan(2 * pi * m / npts)`
- If `k` is 5, the function returns `log(1 + m / npts)`
- If `k` is 7, the function returns `exp(m / npts)`

Restriction: The `return_point` function should be able to handle multiple cases for `k` as specified above.
"""

import math

def return_point(m, npts, k):
    if k == 1:
        return m / npts
    elif k == 2:
        return math.sin(2 * math.pi * m / npts)
    elif k == 3:
        return math.cos(2 * math.pi * m / npts)
    elif k == 4:
        return math.tan(2 * math.pi * m / npts)
    elif k == 5:
        return math.log(1 + m / npts)
    elif k == 7:
        return math.exp(m / npts)