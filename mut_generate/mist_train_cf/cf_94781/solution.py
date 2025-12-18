"""
QUESTION:
Write a function named `find_gcd` that takes an array of integers as input and returns the greatest common divisor (GCD) of all the elements in the array. The GCD is the largest positive integer that divides each of the integers without leaving a remainder. The array may contain both positive and negative integers, duplicate elements, and can have a maximum length of 10^6. The array elements can range from -10^9 to 10^9. If the array is empty, return "Error: Array is empty". If the array contains only one element, return the absolute value of that element. If the array contains only zeros, return 0. The function should not use any built-in functions or libraries for calculating the GCD.
"""

def find_gcd(array):
    if len(array) == 0:
        return "Error: Array is empty"
    elif len(array) == 1:
        return abs(array[0])
    else:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)
        
        result = array[0]
        for i in range(1, len(array)):
            result = gcd(result, array[i])
        
        return result