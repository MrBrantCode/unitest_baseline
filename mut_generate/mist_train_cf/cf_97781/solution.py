"""
QUESTION:
Create a function `divisible_by_3_and_5` that takes a list of integers as input and returns a new list containing only the elements that are divisible by both 3 and 5, but not by 2. The result should be an empty list if there are no such elements. The function must use list comprehension and lambda functions.
"""

def divisible_by_3_and_5(numbers):
    return list(filter(lambda x: x % 3 == 0 and x % 5 == 0 and x % 2 != 0, numbers))