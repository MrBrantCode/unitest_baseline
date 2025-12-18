"""
QUESTION:
Write a function `count_numbers_greater_than_average` that takes a list of integers as input and returns the count of numbers greater than the average of all numbers in the list. If the list is empty, return -1. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the list, and should be implemented using only basic arithmetic operations (+, -, *, /) without using any built-in functions, libraries, sorting algorithms, or additional data structures.
"""

def count_numbers_greater_than_average(lst):
    if len(lst) == 0:
        return -1
    
    total = 0
    for num in lst:
        total += num
    
    average = total / len(lst)
    
    count = 0
    for num in lst:
        if num > average:
            count += 1
    
    return count