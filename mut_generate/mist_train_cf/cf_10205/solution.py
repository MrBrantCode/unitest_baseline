"""
QUESTION:
Create a function called `calculate_average` that takes a list of numbers as input and returns the average of the numbers. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input list.
"""

def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total / count