"""
QUESTION:
Write a function `find_gcd(array)` that takes an array of integers as input and returns the greatest common divisor (GCD) of all the elements in the array. The array may contain both positive and negative integers, and may have a maximum length of 10^6. The array elements can range from -10^9 to 10^9. If the array is empty, return "Array is empty". If the array contains only one element, return the absolute value of the element. If the array contains only zeros, return 0. Otherwise, return the absolute value of the GCD. Do not use any built-in functions or libraries for calculating the GCD.
"""

def find_gcd(array):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)
    
    if len(array) == 0:
        return "Array is empty"
    if len(array) == 1:
        return abs(array[0])
    
    result = abs(array[0])
    for i in range(1, len(array)):
        result = gcd(result, abs(array[i]))
    
    return result