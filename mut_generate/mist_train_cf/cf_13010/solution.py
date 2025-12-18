"""
QUESTION:
Write a recursive function named `factorial` that calculates the factorial of a given number without using the multiplication operator (*). The function should return the factorial of the input number.
"""

def entrance(n):
    def add(a, b):
        if b == 0:
            return a
        else:
            return add(a + 1, b - 1)

    def subtract(a, b):
        if b == 0:
            return a
        else:
            return subtract(a - 1, b - 1)

    if n == 0 or n == 1:
        return 1
    else:
        return add(n, entrance(subtract(n, 1)))