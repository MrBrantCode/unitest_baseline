"""
QUESTION:
Write a function `find_gcd` that calculates the greatest common divisor (GCD) of all elements in a given array of integers. The array can have up to 10^6 elements, and the elements can range from -10^9 to 10^9. The function should return the absolute value of the GCD. Handle the cases where the array is empty, has only one element, or contains only zeros. Do not use any built-in functions or libraries for calculating the GCD.
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def find_gcd(array):
    if len(array) == 0:
        return "Array is empty"
    if len(array) == 1:
        return abs(array[0])
    
    result = abs(array[0])
    for i in range(1, len(array)):
        result = gcd(result, abs(array[i]))
    
    return result