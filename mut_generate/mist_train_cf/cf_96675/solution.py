"""
QUESTION:
Write a function `count_numbers_greater_than_average` that takes a list of integers as input and returns the count of numbers in the list that are greater than the average of all the numbers in the list. The function should handle the case where the list is empty by returning -1. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the list.
"""

def count_numbers_greater_than_average(lst):
    if not lst:
        return -1
    
    total = sum(lst)
    average = total / len(lst)
    count = sum(1 for num in lst if num > average)
    
    return count