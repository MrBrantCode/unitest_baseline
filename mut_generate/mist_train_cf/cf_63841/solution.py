"""
QUESTION:
Create a function named `simplify_fraction` that takes two integer parameters, `numerator` and `denominator`, representing the numerator and denominator of a fraction. The function should return a string representing the simplified fraction in the format "numerator/denominator". The function should handle cases where the numerator is 0 and where the denominator is 1, and should be able to handle large inputs efficiently by using the Euclidean algorithm to calculate the greatest common divisor.
"""

def simplify_fraction(numerator, denominator):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    greatest_common_divisor = gcd(numerator, denominator)
    numerator = numerator // greatest_common_divisor
    denominator = denominator // greatest_common_divisor
    return str(numerator) + "/" + str(denominator)