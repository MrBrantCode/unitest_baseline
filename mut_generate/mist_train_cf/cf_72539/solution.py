"""
QUESTION:
Construct a function called `process_numbers` that takes a list of mixed integers and floating point numbers as input. The function should return two separate lists. The first list should contain the square of each individual integer if the integer is positive, and the second list should store the square root of each individual floating point number if the float is not negative. The function should have a time complexity of O(n) and should use a single loop to process the input list.
"""

import math
def process_numbers(numbers):
    integer_squares = []
    float_roots = []
  
    for num in numbers:
        if isinstance(num, int) and num > 0:
            integer_squares.append(num ** 2)
        elif isinstance(num, float) and num >= 0:
            float_roots.append(math.sqrt(num))
    
    return integer_squares, float_roots