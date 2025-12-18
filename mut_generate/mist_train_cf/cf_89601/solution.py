"""
QUESTION:
Write a function `lcm_of_five_numbers` that takes five positive integers `a`, `b`, `c`, `d`, and `e` as input and returns their least common multiple. You can use the `math.gcd` function from Python's math module to calculate the greatest common divisor.
"""

def lcm_of_five_numbers(a, b, c, d, e):
    lcm_two_numbers = lambda x, y: (x * y) // math.gcd(x, y)
    lcm = lcm_two_numbers(a, b)
    lcm = lcm_two_numbers(lcm, c)
    lcm = lcm_two_numbers(lcm, d)
    lcm = lcm_two_numbers(lcm, e)
    return lcm