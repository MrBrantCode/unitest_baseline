"""
QUESTION:
Create a function named `reverse_string` that takes two parameters: `input_string` and `reversal_value`. The function should reverse `input_string` by `reversal_value` characters to the right if `reversal_value` is positive and to the left if `reversal_value` is negative. The function should handle cases where `reversal_value` is greater than the length of `input_string` or is negative. It should also work with multi-byte characters and special symbols. The function should validate that `input_string` is a non-empty string and `reversal_value` is an integer, and raise an exception otherwise.
"""

def reverse_string(input_string, reversal_value):
    # Input Validation 
    if not isinstance(input_string, str):
        raise Exception("First input must be a string")
    if not isinstance(reversal_value, int):
        raise Exception("Second input must be an integer")
    if not input_string:
        raise Exception("Input string can't be empty")

    # Process in case the reversal_value is more than the string length
    reversal_value = reversal_value % len(input_string)
    
    # Main Algorithm
    input_string = list(input_string)
    if reversal_value > 0:
        for _ in range(reversal_value):
            input_string.insert(0, input_string.pop())
    else:
        for _ in range(abs(reversal_value)):
            input_string.append(input_string.pop(0))
    return ''.join(input_string)