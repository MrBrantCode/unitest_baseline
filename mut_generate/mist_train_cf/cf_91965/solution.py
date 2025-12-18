"""
QUESTION:
Write a function `add_numbers` that takes a list of integers as input and returns their sum without using the addition operator or built-in functions for addition. The function should work with both positive and negative integers and have a time complexity of O(n), where n is the length of the input list.
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