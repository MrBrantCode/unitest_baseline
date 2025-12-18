"""
QUESTION:
Create a function called `xor_binary_numbers` that takes two binary numbers represented as strings (`num1` and `num2`) as input and returns their XOR result as a string. The function should handle binary numbers with a maximum length of 1000 characters and consider leading and trailing zeros.
"""

def xor_binary_numbers(num1, num2):
    # Make sure both binary numbers have the same length
    max_length = max(len(num1), len(num2))
    num1 = num1.zfill(max_length)
    num2 = num2.zfill(max_length)

    # Perform XOR operation
    result = ''
    for i in range(max_length):
        if num1[i] != num2[i]:
            result += '1'
        else:
            result += '0'

    return result