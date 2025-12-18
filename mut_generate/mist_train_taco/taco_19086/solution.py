"""
QUESTION:
This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
"""

def multiply_by_eight_or_nine(number: int) -> int:
    return number * 9 if number % 2 else number * 8