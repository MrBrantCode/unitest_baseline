"""
QUESTION:
Write a function `print_and_return_squares` that takes two integers `start` and `end` and returns a list of squares of numbers between `start` and `end` (inclusive) that are divisible by both 3 and 5, while also printing these squares. The function should have a time complexity of O(n), where n is the number of integers between `start` and `end`. The input range is restricted to -1000 <= `start` <= `end` <= 1000.
"""

def print_and_return_squares(start, end):
    squares = []
    for i in range(start, end+1):
        if i % 3 == 0 and i % 5 == 0:
            square = i ** 2
            squares.append(square)
            print(square)
    return squares