"""
QUESTION:
Develop a function `to_hexadecimal(sequence)` that takes a sequence of numerical inputs and returns their corresponding hexadecimal notations. The function should handle both positive and negative integers, using two's complement for negative numbers. It must also perform error checking, skipping any non-numeric inputs in the sequence.
"""

def to_hexadecimal(sequence):
    hex_sequence = []
    for num in sequence:
        try:
            num = int(num)  # convert to integer if it's not
            if num < 0:  # for negative numbers
                num = num & 0xFFFFFFFF  # taking two's complements into account
            hex_sequence.append(hex(num))
        except ValueError:  # error checking
            print(f"Invalid input: {num}. Skipped.")
            continue
    return hex_sequence