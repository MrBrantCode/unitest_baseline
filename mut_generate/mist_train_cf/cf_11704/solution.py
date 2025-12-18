"""
QUESTION:
Implement a function `add_numbers` that takes a list of integers as input and returns their sum without using built-in addition operators or functions. The function should be able to handle both positive and negative integers and must have a time complexity of O(n), where n is the length of the input list.
"""

def add_numbers(list_of_numbers):
    total = 0
    for num in list_of_numbers:
        if num >= 0:
            while num != 0:
                total += 1
                num -= 1
        else:
            while num != 0:
                total -= 1
                num += 1
    return total