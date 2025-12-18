"""
QUESTION:
Write a function `find_basement_position` that takes a string of "(" and ")" characters as input, representing up and down movements in a building, and returns the 1-indexed position of the character that causes the floor to first reach -1. If the floor never reaches -1, return -1.
"""

def find_basement_position(puzzle_input: str) -> int:
    floor = 0
    for (index, character) in enumerate(puzzle_input, start=1):
        if character == "(":
            floor += 1
        elif character == ")":
            floor -= 1
            if floor == -1:
                return index
    return -1