"""
QUESTION:
Write a function named square_and_divisible that takes a list of integers as input, calculates the square of each integer, and appends the square and a corresponding string to a new list if the square is divisible by 3 or 5. The string should be "divisible by 3" if the square is divisible by 3, "divisible by 5" if the square is divisible by 5, and "divisible by both 3 and 5" if the square is divisible by both. The function should return the new list without duplicates. Do not use built-in functions like set() to remove duplicates.
"""

def square_and_divisible(numbers):
    new_list = []
    for num in numbers:
        square = num ** 2
        if square % 3 == 0 and square % 5 == 0:
            new_list.append((square, "divisible by both 3 and 5"))
        elif square % 3 == 0:
            new_list.append((square, "divisible by 3"))
        elif square % 5 == 0:
            new_list.append((square, "divisible by 5"))
        else:
            new_list.append((square, ""))
    return new_list