"""
QUESTION:
Calculate the sum of squares of numbers in an array using only bitwise operations and loops. The time complexity should be O(n^2) and the solution should use a constant amount of extra space. The array can have duplicates, negative numbers, and can be empty. The only arithmetic operation allowed is the square operation.
"""

def sum_of_squares(arr):
    sum_of_squares = 0
    for num in arr:
        squared_num = num * num
        sum_of_squares += squared_num
    return sum_of_squares