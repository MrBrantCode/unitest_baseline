"""
QUESTION:
Create a function `multiply_odds_by_three` that takes a list of integers as input, multiplies each element by 3, and returns the resulting list, but only if all elements in the input list are positive odd integers.
"""

def multiply_odds_by_three(input_list):
    if all(x > 0 and x % 2 != 0 for x in input_list):
        return list(map(lambda x: x * 3, input_list))
    else:
        return None