"""
QUESTION:
Create a function called `find_squares` that takes two integers `start` and `end` and returns a list of squares of numbers between `start` and `end` inclusive that are divisible by both 3 and 5, and also prints these squares. The function should have a time complexity of O(n), where n is the number of integers between `start` and `end`, and -1000 <= `start` <= `end` <= 1000.
"""

def find_squares(start, end):
    squares = []
    current = start
    while current <= end:
        if current % 3 == 0 and current % 5 == 0:
            square = current * current
            squares.append(square)
            print(square)
        current += 1
    return squares