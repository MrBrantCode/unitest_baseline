"""
QUESTION:
Create a function named `find_positions` that takes an integer `x` and a list of integers `num_list` as input. The function should return a list of all positions (0-indexed) where `x` is found in `num_list`. If `x` is not present in `num_list`, the function should return the string "x does not exist in the list". The function should aim to achieve the optimal time complexity of O(n), where n is the length of `num_list`.
"""

def find_positions(x, num_list):
    positions = [idx for idx, val in enumerate(num_list) if val == x]
    if not positions:
        return "{} does not exist in the list".format(x)
    else:
        return positions