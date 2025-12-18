"""
QUESTION:
Part 2/3 of my kata series. [Part 1](http://www.codewars.com/kata/riemann-sums-i-left-side-rule)

The description changes little in this second part. Here we simply want to improve our approximation of the integral by using trapezoids instead of rectangles. The left/right side rules have a serious bias and the trapezoidal rules averages those approximations! The same assumptions exist but are pasted here for convenience.

- f will always take a single float argument 
- f will always be a "nice" function, don't worry about NaN
- n will always be a natural number (0, N] 
- b > a 
- and n will be chosen appropriately given the length of [a, b] (as in I will not have step sizes smaller than machine epsilon)
- *!!! round answers to the nearest hundredth!!!*
"""

def trapezoidal_integral(f, n, a, b):
    dx = (b - a) / n
    integral_sum = sum(((f(a + i * dx) + f(a + (i + 1) * dx)) / 2 for i in range(n)))
    return round(dx * integral_sum, 2)