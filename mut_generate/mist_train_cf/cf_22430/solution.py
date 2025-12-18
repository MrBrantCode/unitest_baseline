"""
QUESTION:
Write a function `check_occurrences` that takes a list of integers and a target integer as input parameters. The function should return True if the target integer occurs in the list more than twice and False otherwise. The function must have a time complexity of O(n) and cannot use any built-in functions or libraries that provide direct solutions to the problem. The length of the input list is at most 10^6 and the integers in the list are between -10^9 and 10^9.
"""

def check_occurrences(lst, target):
    count = 0
    for num in lst:
        if num == target:
            count += 1
            if count > 2:
                return True
    return False