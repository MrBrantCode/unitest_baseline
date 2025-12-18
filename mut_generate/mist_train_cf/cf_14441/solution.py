"""
QUESTION:
Write a function named `check_occurrence` that takes two input parameters, a list and a number, and returns `True` if the number occurs in the list more than twice, and `False` otherwise. The function must achieve a time complexity of O(n), where n is the length of the list, and cannot use any built-in functions or libraries that provide direct solutions to the problem.
"""

def check_occurrence(lst, number):
    count = 0
    for num in lst:
        if num == number:
            count += 1
            if count > 2:
                return True
    return False