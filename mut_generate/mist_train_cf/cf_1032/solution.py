"""
QUESTION:
Create a function named `gcd` that takes three prime numbers as input: `num1`, `num2`, and `num3`, and returns the greatest common factor (GCF) of the three numbers. The function should have a time complexity of O(n), where n is the largest prime number among the three. The function should not use any built-in Python functions or libraries for calculating the GCF.
"""

def gcd(num1, num2, num3):
    gcf = min(num1, num2, num3)

    while gcf > 1:
        if num1 % gcf == 0 and num2 % gcf == 0 and num3 % gcf == 0:
            return gcf
        gcf -= 1

    return 1