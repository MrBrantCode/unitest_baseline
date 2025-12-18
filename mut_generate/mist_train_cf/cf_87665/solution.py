"""
QUESTION:
Implement a function called `has_even_sum` that takes a list of positive integers as input and returns True if the sum of all the numbers in the list is even, and False otherwise. The implementation must not use any built-in functions or methods for checking if a number is even. The input list will always contain at least one element. The solution should have a time complexity of O(n) and use constant extra space.
"""

def has_even_sum(lst):
    running_sum = 0
    for num in lst:
        running_sum += num
        if running_sum % 2 != 0:  
            return False
    return running_sum % 2 == 0 