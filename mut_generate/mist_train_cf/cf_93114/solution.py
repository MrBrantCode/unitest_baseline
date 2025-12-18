"""
QUESTION:
Create a function `square_and_divisible` that takes a list of integers as input and returns a new list. The new list should contain the square of each number from the original list. For each square, if it's divisible by 3, append "divisible by 3"; if it's divisible by 5, append "divisible by 5"; if it's divisible by both 3 and 5, append "divisible by both 3 and 5". The function should return the new list.
"""

def square_and_divisible(lst):
    new_lst = []
    for num in lst:
        square = num ** 2
        if square % 3 == 0 and square % 5 == 0:
            new_lst.append(str(square) + " divisible by both 3 and 5")
        elif square % 3 == 0:
            new_lst.append(str(square) + " divisible by 3")
        elif square % 5 == 0:
            new_lst.append(str(square) + " divisible by 5")
        else:
            new_lst.append(square)
    return new_lst