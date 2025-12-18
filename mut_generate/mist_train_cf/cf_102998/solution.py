"""
QUESTION:
Implement a function `find_gcd(arr)` that calculates the greatest common divisor (GCD) of all elements in the given array. The array may contain both positive and negative integers, and the function should return the absolute value of the GCD. The function should handle the following edge cases: 

- An empty array, in which case it should return an error message.
- An array with one element, in which case it should return the absolute value of the element.
- An array with all elements being zero, in which case it should return zero.
- An array with both positive and negative integers.
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