"""
QUESTION:
Create a function 'checkInteger' that takes a single argument, a number, and returns True if the number is an integer within the range -10^9 to 10^9, False otherwise.
"""

def checkInteger(number):
    return isinstance(number, int) and -10**9 <= number <= 10**9