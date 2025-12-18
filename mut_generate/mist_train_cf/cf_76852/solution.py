"""
QUESTION:
Implement a function `intricate_rounding(value, low, high, exclude, duplicates)` that takes a string signifying a number, a pair of integers as range limits, a list of integers to exclude, and a boolean indicating whether to check for duplicates. The function should return the closest integer to the input value using a custom rounding logic, where if the provided number is at equal distance from two integers, it returns the one closer to zero. If the input value is not a valid integer or float within the given range, or if the rounded integer is in the exclude list or a duplicate, the function should return an error message.
"""

def intricate_rounding(value, low, high, exclude, duplicates):
    try:
        value = float(value)
    except ValueError:
        return "錯誤：無效的輸入。"

    if not low <= value <= high:
        return "錯誤：超出範圍。"

    if value - int(value) < 0.5:
        round_int = int(value)
    elif value < 0 and value - int(value) == 0.5:
        round_int = int(value)
    else:
        round_int = int(value) + 1

    if round_int in exclude or (duplicates and round_int == value):
        return "Error: Duplicate or number in excluded list."
    return round_int