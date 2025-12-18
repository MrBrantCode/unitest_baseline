"""
QUESTION:
Implement a function `calculate_polynomial_value(x, n)` that calculates the value of a polynomial at a given abscissa `x` (integer) for a given polynomial order `n` (integer), defined by the recurrence relation: 
\[ P_n(x) = \begin{cases} 
      1 & \text{if } n = 0 \\
      x & \text{if } n = 1 \\
      2xP_{n-1}(x) - P_{n-2}(x) & \text{if } n > 1 
   \end{cases}
\]
The function should return the value of the polynomial at the given abscissa and order.
"""

def calculate_polynomial_value(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        prev_prev = 1
        prev = x
        for i in range(2, n + 1):
            current = 2 * x * prev - prev_prev
            prev_prev = prev
            prev = current
        return current