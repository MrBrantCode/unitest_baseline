"""
QUESTION:
Write a function named `find_gcd(arr)` that calculates the greatest common divisor (GCD) of all elements in the given array `arr`. The array may contain both positive and negative integers and may include duplicate elements. The GCD is the largest positive integer that divides each of the integers without leaving a remainder. You are not allowed to use any built-in functions or libraries for calculating the GCD. Handle the cases when the array is empty, contains only one element, contains only zeros, or contains both positive and negative integers, and return the absolute value of the GCD in these cases.
"""

def find_gcd(arr):
    if len(arr) == 0:
        return "Error: Array is empty."
    if len(arr) == 1:
        return abs(arr[0])

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)

    result = arr[0]
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])

    return result