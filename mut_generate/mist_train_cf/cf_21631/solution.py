"""
QUESTION:
Write a function `count_numbers_greater_than_average` that takes a list of integers as input and returns the count of numbers greater than the average of the list. The function should handle the case when the list is empty by returning -1. The time complexity should be O(n) and the space complexity should be O(1), where n is the length of the list.
"""

def count_numbers_greater_than_average(lst):
    if not lst:
        return -1
    
    total = sum(lst)
    average = total / len(lst)
    count = 0
    
    for num in lst:
        if num > average:
            count += 1
    
    return count