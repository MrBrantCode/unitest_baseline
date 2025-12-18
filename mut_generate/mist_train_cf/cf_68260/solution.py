"""
QUESTION:
Write a function `find_divisors_gcd_lcm` that accepts two integers `X` and `Y` as input. The function should output every positive divisor for both `X` and `Y`, the common divisors between them, the greatest common divisor (GCD) of `X` and `Y`, and the least common multiple (LCM) of `X` and `Y`. The input integers `X` and `Y` are positive.
"""

def find_divisors_gcd_lcm(X, Y):
    def find_divisors(num):
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors

    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    def lcm(x, y):
        lcm = (x*y)//gcd(x,y)
        return lcm

    divisors_X = find_divisors(X)
    divisors_Y = find_divisors(Y)
    common_divisors = list(set(divisors_X) & set(divisors_Y))
    GCD = gcd(X, Y)
    LCM = lcm(X, Y)

    return divisors_X, divisors_Y, common_divisors, GCD, LCM