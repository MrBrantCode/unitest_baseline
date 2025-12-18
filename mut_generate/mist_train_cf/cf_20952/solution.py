"""
QUESTION:
Implement a function `calculate_sum` that takes a list of numbers as input and returns the sum of all numbers in the list. The function should have a time complexity of O(n), where n is the number of elements in the list, and a space complexity of O(1), using constant extra space regardless of the input size. The function must not use built-in sum functions, libraries, or the '+' operator for addition.
"""

def calculate_sum(numbers):
    sum = 0
    for num in numbers:
        sum = sum - (-num)
    return sum