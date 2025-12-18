"""
QUESTION:
Write a function named `xor_binary_numbers` that takes two binary numbers as strings, each up to 1000 characters long, and returns their XOR result as a string. The function should handle binary numbers with leading zeros and trailing zeros by padding the shorter string with zeros from the left to match the length of the longer string.
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