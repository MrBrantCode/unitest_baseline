"""
QUESTION:
Implement a function called `has_even_sum` that takes a list of positive integers as input and returns True if the sum of all the numbers in the list is even, and False otherwise. The implementation must not use any built-in functions or methods for checking if a number is even. The function should have a time complexity of O(n) and use constant extra space, where n is the length of the input list.
"""

def has_even_sum(lst):
    running_sum = 0
    for num in lst:
        running_sum += num
        if running_sum % 2 != 0:  # check if running sum is odd
            return False
    return running_sum % 2 == 0  # check if final sum is even