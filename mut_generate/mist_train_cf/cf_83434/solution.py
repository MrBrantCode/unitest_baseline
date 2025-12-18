"""
QUESTION:
Create a function `dec_to_bin` that takes a decimal number (1-1000) as input and returns its binary representation, the binary representation in reverse order, and the binary representation in 8-bit format (with leading zeros). The function should handle user input errors by accepting integers provided in strings, checking for valid integers, and validating numbers within the range 1-1000.
"""

def dec_to_bin(num):
    try:
        num=int(num)
        if num>=1 and num<=1000:
            num_bin=bin(num)[2:]    #Transforms the number to binary
            num_8_bit = num_bin.zfill(8)   #Transforms to the 8 bit representation
            num_reversed=num_bin[::-1]   #Reverses the binary number
            return (num_bin, num_8_bit, num_reversed)
        else:
            return 'The number must be between 1 and 1000'
    except:
        return 'Invalid parameter. The input must be an integer.'