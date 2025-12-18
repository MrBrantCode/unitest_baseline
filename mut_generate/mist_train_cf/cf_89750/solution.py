"""
QUESTION:
Write a function `count_numbers_greater_than_average(lst)` that takes a list of integers `lst` as input and returns the count of numbers greater than the average of all numbers in the list. If the list is empty, return -1. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the list. The implementation should use a single pass over the list (with the exception of calculating the average), not use any built-in functions or libraries to calculate the average, not use any additional data structures such as dictionaries or sets, handle negative numbers correctly, handle large input sizes efficiently, and use only basic arithmetic operations.
"""

def count_numbers_greater_than_average(lst):
    if len(lst) == 0:
        return -1
    
    total = 0
    for num in lst:
        total += num
    
    average = total / len(lst)
    
    count = sum(1 for num in lst if num > average)
    
    return count