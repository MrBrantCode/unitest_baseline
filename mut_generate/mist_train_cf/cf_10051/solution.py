"""
QUESTION:
Write a function in Python to determine if an integer is even or odd without using the modulo operator (%). The function should take an integer as input and return a boolean value (True or False) indicating whether the number is even or odd. Use bitwise operations to solve the problem.
"""

def entrance(num):
    if num & 1 == 0:
        return True
    else:
        return False