"""
QUESTION:
Create a function named `multiply_by_smallest_prime` that takes an array of integers as input. The function should multiply each element in the array by the smallest prime number greater than 3 and return the new array. The smallest prime number greater than 3 is 5, so the function should multiply each element by 5.
"""

def multiply_by_smallest_prime(arr):
    prime = 5
    multiplied_arr = []
    for num in arr:
        multiplied_arr.append(num * prime)
    return multiplied_arr