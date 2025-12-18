"""
QUESTION:
Write a function named `solve` that takes an array of integers as input and returns an array where each element at the i'th position is the product of all units in the input array excluding the integer at the i'th position. The function should have a time complexity of O(n) and not use division.
"""

def solve(numbers):
    length = len(numbers)
    result = [0] * length
    temp = 1

    # calculate the cumulative product from left to right
    left_prod = [1] * length
    for i in range(length):
        left_prod[i] = temp
        temp *= numbers[i]

    # calculate the cumulative product from right to left
    temp = 1
    right_prod = [1] * length
    for i in range(length - 1, -1, -1):
        right_prod[i] = temp
        temp *= numbers[i]

    # multiply the corresponding elements in left_prod and right_prod to get the answer
    for i in range(length):
        result[i] = left_prod[i] * right_prod[i]

    return result