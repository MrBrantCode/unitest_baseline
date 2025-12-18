"""
QUESTION:
Create a function `create_squared_dict(n)` that generates a dictionary where keys are numbers from 1 to n and values are their squares, excluding perfect squares. The function should also return the sum of all squares in the dictionary.
"""

def create_squared_dict(n):
    squared_dict = {}
    sum_of_squares = 0

    for i in range(1, n+1):
        square = i ** 2
        if round(square ** 0.5) ** 2 != square:
            squared_dict[i] = square
            sum_of_squares += square
    
    return squared_dict, sum_of_squares