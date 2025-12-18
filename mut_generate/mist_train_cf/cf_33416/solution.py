"""
QUESTION:
Calculate the sum of the products of adjacent pairs of integers in a list. The list is treated as circular, meaning that the "next" integer of the last integer is the first integer in the list.

Write a function `sum_of_adjacent_products(puzzle_input)` where `puzzle_input` is a list of integers with a length between 2 and 1000 (inclusive). The function should return the sum of the products of adjacent pairs of integers in the input list.
"""

def entrance(puzzle_input):
    total = 0
    for cur_index in range(len(puzzle_input)):
        next_index = cur_index + 1 if not cur_index == len(puzzle_input) - 1 else 0
        total += puzzle_input[cur_index] * puzzle_input[next_index]
    return total