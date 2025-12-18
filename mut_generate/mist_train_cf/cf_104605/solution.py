"""
QUESTION:
Write a function `findSecondLargest` that finds the second largest number in an array of integers with a time complexity of O(n). The function should return the second largest number in the array.
"""

def findSecondLargest(numbers):
    if len(numbers) < 2:
        return None

    max_num = second_max = float('-inf')

    for num in numbers:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num < max_num:
            second_max = num

    if second_max == float('-inf'):
        return None

    return second_max