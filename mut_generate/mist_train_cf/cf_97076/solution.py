"""
QUESTION:
Write a function `check_occurrences` that takes a list of integers and a target integer as input parameters, and returns `True` if the target integer occurs in the list more than twice and `False` otherwise. The function should have a time complexity of O(n) and not use any built-in functions or libraries that provide direct solutions to the problem. The input list has at most 10^6 elements, and the integers in the list and the target integer are between -10^9 and 10^9.
"""

def check_occurrences(lst, target):
    count = 0
    for num in lst:
        if num == target:
            count += 1
            if count > 2:
                return True
    return False