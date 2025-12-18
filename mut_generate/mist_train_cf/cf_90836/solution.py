"""
QUESTION:
Implement a function called `sum_of_list` that calculates the sum of the numbers in a given list. The function should have a time complexity of O(n), where n is the length of the list, and should not use any built-in Python functions or libraries that directly calculate the sum of a list, nor recursion.
"""

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total