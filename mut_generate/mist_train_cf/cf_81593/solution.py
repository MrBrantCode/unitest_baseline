"""
QUESTION:
Create a function named `gcd_lcm(num1, num2)` that takes two numbers as input and returns the greatest common divisor (GCD) and least common multiple (LCM) of the two numbers. The function should handle edge cases, including when one number is zero or both numbers are the same. The function should be optimized to handle numbers up to 1 million.
"""

def gcd_lcm(num1, num2):
    if num1 == 0 and num2 == 0:
        return 0, 0
    
    if num1 == 0:
        return num2, 0
    
    if num2 == 0:
        return num1, 0
    
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    return gcd(num1, num2), lcm(num1, num2)