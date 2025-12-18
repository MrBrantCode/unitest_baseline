"""
QUESTION:
Write a function named `find_max` that takes four numbers as input and returns the maximum of the four numbers using nested if statements.
"""

def find_max(num1, num2, num3, num4):
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    if num4 > max_num:
        max_num = num4
    return max_num