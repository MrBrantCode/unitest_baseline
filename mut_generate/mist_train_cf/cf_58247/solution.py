"""
QUESTION:
Write a function `count_toys` that takes a binary code as a string of 0's and 1's as input, representing the arrangement of puzzle games (0) and dolls (1) in a toy franchise store. The store's total number of puzzle games and dolls follows a ratio of 5:3. The function should return the number of puzzle games and dolls in the store.
"""

def count_toys(binary_code):
    total_toys = len(binary_code)
    ratio_sum = 5 + 3
    puzzle_games = total_toys * 5 // ratio_sum
    dolls = total_toys * 3 // ratio_sum
    return puzzle_games, dolls