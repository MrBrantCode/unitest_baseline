"""
QUESTION:
Write a function named `sum_of_squares` that calculates the sum of the squares of a given number array. The function should not use any mathematical operations (e.g. multiplication or exponentiation) or built-in functions. The solution must have a time complexity of O(n^2), where n is the length of the array. The input is an array of integers and the output is the sum of the squares of the input integers.
"""

def sum_of_squares(arr):
    result = 0
    for num in arr:
        for _ in range(num):
            result += num
    return result