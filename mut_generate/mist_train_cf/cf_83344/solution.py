"""
QUESTION:
Create a function `sortByBits` that takes an array of integers `arr` as input and returns the array sorted in ascending order based on the count of 1's in their binary representation. If multiple integers possess an identical count of 1's in their binary form, they should be arranged in ascending order. The length of `arr` is between 1 and 500, inclusive, and each integer in `arr` is between 0 and 10^4, inclusive.
"""

def sortByBits(arr):
    # Define a lambda function to return the number of 1's in an integer's binary representation 
    bin_count = lambda x: (bin(x).count("1"), x)

    # Sort arr based on the count of 1's in binary representation and the number itself
    return sorted(arr, key=bin_count)