"""
QUESTION:
Write a function `binarySum` that takes two binary numbers `bin_num1` and `bin_num2` as input strings and returns their sum as a binary string without using any built-in binary conversion functions. The input binary numbers can be of different lengths.
"""

def binarySum(bin_num1, bin_num2):

    # Initialize variables
    max_len = max(len(bin_num1), len(bin_num2))
    binary_sum = ''
    carry = 0

    # Pad the shorter binary number with zeros to have equal length
    bin_num1 = bin_num1.zfill(max_len)
    bin_num2 = bin_num2.zfill(max_len)

    # Iterate from the last digit until the first digit
    for i in range(max_len-1, -1, -1):
        bit_sum = carry
        bit_sum += 1 if bin_num1[i]=='1' else 0
        bit_sum += 1 if bin_num2[i]=='1' else 0
        
        binary_sum = ('1' if bit_sum % 2 == 1 else '0') + binary_sum

        carry = 0 if bit_sum < 2 else 1 # Update carry
        
    if carry != 0 : binary_sum = '1' + binary_sum 

    return binary_sum.zfill(max_len)