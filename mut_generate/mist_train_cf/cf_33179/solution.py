"""
QUESTION:
Implement the function `are_dice_compatible(die1, die2)` that takes in two integers `die1` and `die2` representing the values of two dice. The function should return `True` if the dice are compatible based on the following conditions:

- If neither die1 nor die2 contains both 3 and 6, and neither contains both 3 and 9, they are not compatible.
- If neither die1 nor die2 contains both 4 and 9, and neither contains both 4 and 6, they are not compatible.
- If neither die1 nor die2 contains both 6 and 4, and neither contains both 9 and 4, they are not compatible.
- If neither die1 nor die2 contains both 8 and 1, they are not compatible.
- If none of the above conditions are met, the dice are compatible.

The function should return `True` if the dice are compatible and `False` otherwise.
"""

def are_dice_compatible(die1: int, die2: int) -> bool:
    def digits_match(digit1: int, digit2: int) -> bool:
        return (str(digit1) in str(die1) and str(digit2) in str(die1)) or (str(digit1) in str(die2) and str(digit2) in str(die2))

    if not digits_match(3, 6) and not digits_match(3, 9):
        return False
    if not digits_match(4, 9) and not digits_match(4, 6):
        return False
    if not digits_match(6, 4) and not digits_match(9, 4):
        return False
    if not digits_match(8, 1):
        return False
    return True