"""
QUESTION:
Write a function called `calculate_bricks_required` that determines the maximum number of bricks required to cover a rectangular patio with no leftovers. The function should take four parameters: `patio_length_inches`, `patio_width_inches`, `brick_length_inches`, and `brick_width_inches`, representing the dimensions of the patio and the bricks in inches.
"""

def calculate_bricks_required(patio_length_inches, patio_width_inches, brick_length_inches, brick_width_inches):
    patio_area = patio_length_inches * patio_width_inches
    brick_area = brick_length_inches * brick_width_inches
    required_bricks = patio_area / brick_area
    return int(required_bricks)