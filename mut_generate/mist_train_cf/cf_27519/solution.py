"""
QUESTION:
Implement a function `quantized_bias_add` that takes four parameters: `input_val`, `bias`, `int_bits`, and `frac_bits`, and returns the result of adding the `bias` to the `input_val` considering a fixed-point representation with `int_bits` integer bits and `frac_bits` fractional bits. The function should handle the addition and scaling of the input and bias values to match the specified fixed-point representation.
"""

def quantized_bias_add(input_val: int, bias: int, int_bits: int, frac_bits: int) -> int:
    # Calculate the scaling factor based on the number of fractional bits
    scale_factor = 2 ** frac_bits

    # Scale the input and bias to align with the fixed-point representation
    scaled_input = input_val * scale_factor
    scaled_bias = bias * scale_factor

    # Perform the bias addition in the scaled domain
    result = scaled_input + scaled_bias

    # Adjust the result to the original fixed-point representation
    result = result // scale_factor

    return result