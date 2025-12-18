"""
QUESTION:
Create a function named `extract_integer` that takes two parameters: a float `number` and a boolean `round_down` with a default value of `True`. The function should return the integer part of the number, either rounded down (if `round_down` is `True`) or rounded up (if `round_down` is `False`). The function should be able to handle both positive and negative numbers.
"""

def extract_integer(number: float, round_down: bool = True) -> int:
    if round_down:
        if number >= 0:
            return int(number)
        else:
            return int(number) - 1
    else:
        if number >= 0:
            return int(number) + 1 if number % 1 != 0 else int(number)
        else:
            return int(number)