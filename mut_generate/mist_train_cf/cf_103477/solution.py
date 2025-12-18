"""
QUESTION:
Write a function `calculate_average` that takes an array of integers as input and returns the average of the array. The function should be able to handle both positive and negative integers, have a time complexity of O(n), and a space complexity of O(1). If the input array is empty, the function should return 0.
"""

def calculate_average(numbers):
    n = len(numbers)
    if n == 0:
        return 0

    sum = 0
    for num in numbers:
        sum += num

    return sum / n