"""
QUESTION:
Calculate the sum of squares of the given number array without using mathematical operations (multiplication or exponentiation) or built-in functions, and achieve a time complexity of O(n^2). Implement the function `sum_of_squares(arr)` where `arr` is the input array of integers.
"""

def calculate_sum_of_squares(arr):
    result = 0
    for num in arr:
        square = 0
        for _ in range(abs(num)):
            square += num
        result += square if num > 0 else -square
    return result