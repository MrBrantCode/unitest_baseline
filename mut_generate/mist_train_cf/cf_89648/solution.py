"""
QUESTION:
Create a function named `find_squares` that takes two integers, `start` and `end`, and prints out the square of the numbers between `start` and `end`, inclusive. However, only print the square if the number is divisible by both 3 and 5. Additionally, the function should return a list of all the squares that were printed.

Constraints: 
-1000 <= `start` <= `end` <= 1000 
The function should have a time complexity of O(n), where n is the number of integers between `start` and `end`.
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