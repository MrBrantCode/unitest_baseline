"""
QUESTION:
Write a function named `find_gcd` that takes an array of integers as input. The function should calculate the greatest common divisor (GCD) of all elements in the array, handling cases where the array may be empty, contain duplicate elements, or include both positive and negative integers. The GCD should be the largest positive integer that divides each of the integers without leaving a remainder, and its absolute value should be returned. The array can have a maximum length of 10^6, and its elements can range from -10^9 to 10^9.
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