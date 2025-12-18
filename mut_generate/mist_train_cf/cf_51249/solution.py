"""
QUESTION:
Write a function `binaryOperations(num, add_num)` that takes an integer `num` and a binary string `add_num` as input. The function should first convert the decimal number `num` to a binary string, then perform the following operations: count the total number of 1's and 0's, switch the most significant bit, reverse the binary string, and add the binary number `add_num` to the original binary number. Finally, convert the resulting binary string back to a decimal number and return it.
"""

def binaryOperations(num, add_num):
    # Convert decimal number to binary string
    binary_num = bin(num)[2:]

    # Count the total number of 1's and 0's in the binary string.
    count_1 = binary_num.count('1')
    count_0 = binary_num.count('0')
    
    # Switch the most significant bit
    if binary_num[0] == '1':
        binary_num = '0' + binary_num[1:]
    else:
        binary_num = '1' + binary_num[1:]

    # Reverse the binary string
    binary_num = binary_num[::-1]

    # Add another binary number to the original binary number
    result = bin(int(binary_num, 2) + int(add_num, 2))[2:]

    # Convert back to decimal
    decimal_num = int(result, 2)
    return decimal_num