"""
QUESTION:
Implement a function `find_gcd(arr)` that calculates the greatest common divisor (GCD) of an array of integers. The function should take an array of integers as input and return their GCD. The GCD is the largest number that divides each of the integers in the array without a remainder.
"""

def find_gcd(arr):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    result = arr[0]
    for i in arr[1:]:
        result = gcd(result, i)
    return result