"""
QUESTION:
Create a function called `sumOddHelper` that recursively calculates the sum of all odd numbers in a given array with a time complexity of O(n), without using built-in functions for summation or checking odd numbers. The function should take in the array, current index, and running sum as parameters.
"""

def sumOddHelper(data, index, total):
    if index == len(data):
        return total
    else:
        if data[index] % 2 != 0:
            total += data[index]
        return sumOddHelper(data, index + 1, total)