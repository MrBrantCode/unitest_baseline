"""
QUESTION:
Write a function `check_direction(cw_direction)` that takes a list of integers `cw_direction` representing clockwise directions (0 for north, 1 for east, 2 for south, 3 for west) and returns "error" if the sum of the directions is greater than half the length of the list; otherwise, return the sum of the directions.
"""

def entrance(cw_direction):
    if sum(cw_direction) > (len(cw_direction) / 2):
        return "error"
    else:
        return sum(cw_direction)