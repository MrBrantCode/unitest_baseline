"""
QUESTION:
Create a function `check_divisibility` that takes a list of integers and returns True if all integers in the list are divisible by both 7 and 5.
"""

def check_divisibility(lst):
    for num in lst:
        if num % 7 != 0 or num % 5 != 0:
            return False
    return True