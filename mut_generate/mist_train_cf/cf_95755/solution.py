"""
QUESTION:
Write a function called `calculate_average` that takes a list of numbers as input and returns the average of all elements in the list. The function must have a time complexity of O(n) and use a constant amount of extra space. It should also be able to handle both negative and floating-point numbers.
"""

def calculate_average(lst):
    total = 0
    count = 0

    for num in lst:
        total += num
        count += 1

    average = total / count
    return average