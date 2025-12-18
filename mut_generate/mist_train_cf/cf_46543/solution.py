"""
QUESTION:
Construct the function `constructRectangle` to design a rectangular web page with the given area. The function takes one argument, `area`, and returns an array `[L, W]` where `L` and `W` are the length and width of the web page, satisfying the following requirements:
- The area of the rectangular web page is equal to the given target area.
- The width `W` is not larger than the length `L`, i.e., `L >= W`.
- The difference between length `L` and width `W` is as small as possible.
- The length `L` and width `W` are prime numbers.
If no such rectangle can be found, return an empty array.
The input `area` is an integer and `1 <= area <= 10^7`.
"""

import math

def constructRectangle(area):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(int(math.sqrt(area)), 0, -1):
        if area % i == 0 and (is_prime(i) and is_prime(area // i)):
            return [area // i, i] if area // i >= i else [i, area // i]
    if is_prime(area):
        return [area, 1]
    return []