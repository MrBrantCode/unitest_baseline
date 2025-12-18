"""
QUESTION:
Create a function `create_squares_dictionary(n)` that generates a dictionary containing the squares of numbers up to `n`, excluding perfect squares, and returns the dictionary along with the sum of its values. The function should exclude numbers where the square is equal to the number itself.
"""

def create_squares_dictionary(n):
    squares_dict = {}
    square_sum = 0
    for num in range(1, n+1):
        square = num**2
        if square != num:
            squares_dict[num] = square
            square_sum += square
    return squares_dict, square_sum