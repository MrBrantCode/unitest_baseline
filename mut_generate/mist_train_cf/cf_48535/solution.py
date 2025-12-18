"""
QUESTION:
Create a function `array_to_binary(arr)` that takes an array of integers `arr` as input, converts each integer into its binary representation as a string of 8 bits (padding with zeros to the left if necessary), and returns the resulting array of binary strings.
"""

def array_to_binary(arr):
    binary_arr = []
    for num in arr:
        binary_arr.append(format(num, '08b'))
    return binary_arr