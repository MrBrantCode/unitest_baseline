"""
QUESTION:
Write a function called `largest_common_denominator` that takes two integers `a` and `b` as input, and two divisors `divisor1` and `divisor2`. The function should return the largest common denominator of `a` and `b` that is divisible by both `divisor1` and `divisor2`.
"""

def largest_common_denominator(a, b, divisor1, divisor2):
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    def lcm(x, y):
        lcm = (x*y)//gcd(x,y)
        return lcm

    def is_divisible(n, divisor1, divisor2):
        return n % divisor1 == 0 and n % divisor2 == 0

    lcm_ab = lcm(a, b)
    gcd_ab = gcd(a, b)

    common_denominators = [i for i in range(gcd_ab, 0, -1) if a % i == 0 and b % i == 0]
    
    for denominator in common_denominators:
        if is_divisible(denominator, divisor1, divisor2):
            return denominator