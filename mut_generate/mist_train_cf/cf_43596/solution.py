"""
QUESTION:
Implement the function `compute_gcd(num1, num2)` to find the greatest common divisor (GCD) of two integers `num1` and `num2`. The function should return the largest number that divides both `num1` and `num2` without leaving a remainder. Ensure that the function works for any pair of positive integers.
"""

def compute_gcd(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1  

    gcd = 1  

    for i in range(1, num1 + 1):  
        if num1 % i == 0 and num2 % i == 0:  
            gcd = i  
    return gcd