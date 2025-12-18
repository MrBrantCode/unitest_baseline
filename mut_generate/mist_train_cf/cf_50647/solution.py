"""
QUESTION:
Write a function named `array_multiply_add` that takes an array of integers and two additional integers as parameters. The function should multiply each element in the array by the two integers, sum the results, and return the sum. The array can contain up to 10^6 integers, and the two integers can range from 1 to 100.
"""

def array_multiply_add(array, multiplier1, multiplier2):
    multiplier = multiplier1 * multiplier2
    return sum([num * multiplier for num in array])