"""
QUESTION:
Write a function to find the minimum positive integer that can be evenly distributed by the factors of three given numbers without leaving any remainder or fractional value. The function should take three integers as input and return the Least Common Multiple (LCM) of these numbers.
"""

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def find_lcm(num1, num2, num3):
    def lcm(x, y):
        return (x*y)//gcd(x,y)
    
    lcm1n2 = lcm(num1, num2)
    return lcm(lcm1n2, num3)