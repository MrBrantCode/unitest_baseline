"""
QUESTION:
Create a function called `generate_multiplication_table` that takes three parameters: `number`, `range_start`, and `range_end`. The function should generate a multiplication table for the given `number` within the range from `range_start` to `range_end` (inclusive), excluding even numbers. The table should be returned as a string in the format "i x number = i * number" for each odd number `i` in the range.
"""

def generate_multiplication_table(number, range_start, range_end):
    table = ""
    for i in range(range_start, range_end + 1):
        if i % 2 != 0:
            table += f"{i} x {number} = {i * number}\n"
    return table