"""
QUESTION:
Create a function named `edit_list` that takes a list of integers as input and returns a new list containing only the even numbers greater than 4, in ascending order. The function should maintain a time complexity of O(n log n) and a space complexity of O(n), although the space complexity can be increased if necessary.
"""

def edit_list(numbers):
    result = [num for num in numbers if num % 2 == 0 and num > 4]
    result.sort()
    return result