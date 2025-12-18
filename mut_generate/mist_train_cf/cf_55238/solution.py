"""
QUESTION:
Given the number of `tomatoSlices`, `cheeseSlices`, and `timeLimit`, find the number of jumbo and small burgers that can be made without wasting any ingredients and within the given time limit. Each jumbo burger requires 4 tomato slices, 1 cheese slice, and takes 2 minutes, while each small burger requires 2 tomato slices, 1 cheese slice, and takes 1 minute. The function `numOfBurgers` should return a list `[total_jumbo, total_small]` if possible, otherwise an empty list `[]`. The constraints are `0 <= tomatoSlices, cheeseSlices, timeLimit <= 10^7`.
"""

def numOfBurgers(tomatoSlices: int, cheeseSlices: int, timeLimit: int) -> list[int]:
    if 4 * cheeseSlices > tomatoSlices or tomatoSlices > 2 * timeLimit or tomatoSlices % 2 != 0 or cheeseSlices > timeLimit:
        return []
    total_jumbo = 2*cheeseSlices - tomatoSlices // 2
    total_small = cheeseSlices - total_jumbo
    if total_jumbo < 0 or total_small < 0 or 2*total_jumbo + total_small > timeLimit:
        return []
    return [total_jumbo, total_small]