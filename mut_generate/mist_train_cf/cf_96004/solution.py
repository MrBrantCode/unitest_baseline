"""
QUESTION:
Write a function `average_positive` that calculates the average of positive integers in an array of n numbers. The function should ignore non-positive integers and return 0 if there are no positive integers. The function must have a time complexity of O(n) and a space complexity of O(1).
"""

def average_positive(arr):
    positive_sum = 0
    positive_count = 0

    for num in arr:
        if num > 0:
            positive_sum += num
            positive_count += 1

    if positive_count == 0:
        return 0  

    return positive_sum / positive_count