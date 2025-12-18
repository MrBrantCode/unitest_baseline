"""
QUESTION:
Write a function `multiply_by_smallest_prime(arr)` that takes an array of integers as input, multiplies each element by the smallest prime number greater than 3 (which is 5), and returns the new array.
"""

def multiply_by_smallest_prime(arr):
    prime = 5
    multiplied_arr = []
    for num in arr:
        multiplied_arr.append(num * prime)
    return multiplied_arr