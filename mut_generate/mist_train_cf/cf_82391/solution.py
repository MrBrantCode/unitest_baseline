"""
QUESTION:
Create a function `find_gcd` that takes two arrays of 1000 random integers between 0 and 1000 as input. The function should return a new array where each element is the greatest common divisor (GCD) of the corresponding elements in the input arrays. The function can only use basic arithmetic operations and loops; external libraries and built-in GCD functions are not allowed.
"""

def find_gcd(arr1, arr2):
    def gcd(a, b):
        if a == 0 or b == 0:
            return a + b
        return gcd(b, a % b)

    return [gcd(a, b) for a, b in zip(arr1, arr2)]