"""
QUESTION:
Design a recursive function `lcm_list` to calculate the least common multiple (LCM) of a given list of integers. The function should handle edge cases such as non-numeric values and zero values. The input list may contain multiple integers. If the list contains non-integer or zero values, return an error message instead of the LCM.
"""

import math
from functools import reduce

def lcm_list(numbers):
    try:
        # Check if all elements in the list are integers.
        for number in numbers:
            if not isinstance(number, int):
                print("Error: The list should contain only integers.")
                return

        # Check if there's a zero in the list.
        if 0 in numbers:
            print("Error: Zero doesn't have a defined LCM.")
            return

        # Calculate LCM
        return reduce(lambda a, b: abs(a*b) // math.gcd(a, b), numbers, 1)
    except Exception as e:
        print(f"Error: {e}")