"""
QUESTION:
Write a function named `check_occurrence` that takes a list of elements and a target number as input parameters. The function should return `True` if the target number occurs in the list more than twice and `False` otherwise. Implement this function without using any built-in functions or libraries that directly solve the problem, and achieve a time complexity of O(n), where n is the length of the list.
"""

def check_occurrence(lst, number):
    count = 0
    for num in lst:
        if num == number:
            count += 1
            if count > 2:
                return True
    return False